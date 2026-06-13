import re

def parse_items(content, start_keyword, end_keyword):
    lines = content.split('\n')
    found = False
    items = []
    for line in lines:
        if start_keyword in line and not found:
            found = True
            continue
        if found:
            if end_keyword in line or not line.strip():
                if end_keyword in line: break
                # For empty lines, we just skip unless it's the marker for next section
                continue
            if line.startswith('-'):
                # Format: - 1150202 跨行轉入 C 3 - 3 管理 ：12,848
                parts = line[2:].rsplit('：', 1)
                if len(parts) == 2:
                    desc = parts[0].strip()
                    amount = parts[1].strip()
                    # Split date from description
                    date_match = re.match(r'^(\d+)\s+(.*)', desc)
                    if date_match:
                        items.append({
                            'date': date_match.group(1),
                            'description': date_match.group(2),
                            'amount': amount
                        })
                    else:
                        items.append({
                            'date': '',
                            'description': desc,
                            'amount': amount
                        })
    return items

with open('finance.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract Income sections
general_income = parse_items(content, '**一般收入**', '其他收入小計')
other_income = parse_items(content, '**其他收入**', '收入合計')

# Extract Expense sections
fixed_expense = parse_items(content, '**固定支出**', '固定支出小計')
variable_expense = parse_items(content, '**非固定支出**', '支出合計')

# Summary values
summary_data = {}
sums = ['上期結餘', '本期收入', '本期支出', '本期結餘']
for s in sums:
    match = re.search(rf'- \*\* {s} \*\*: ([\d,]+)', content) # Note the regex needs to match exactly'**上期結餘**：2,575,225'
    # Adjusted regex for current finance.md format "- **上期結餘**：2,575,225"
    match = re.search(rf'- \*\*{s}\*\*：([\d,]+)', content)
    if match:
        summary_data[s] = match.group(1)

def generate_table(items):
    if not items: return ""
    table = "| 日期 | 項目 | 金額 |\n| --- | --- | --- |\n"
    for item in items:
        table += f"| {item['date']} | {item['description']} | {item['amount']} |\n"
    return table

output = "## 財務報表 (表格版)\n\n---\n### 收支表格\n\n#### 收入項目\n---\n**一般收入**\n"
output += generate_table(general_income)
# Need to find the subtotal from content for accuracy
gen_sub = re.search(r'一般收入小計：([\d,]+)', content).group(1)
output += f"\n**一般收入小計：{gen_sub}**\n\n"

output += "**其他收入**\n"
output += generate_table(other_income)
oth_sub = re.search(r'其他收入小計：([\d,]+)', content).group(1)
output += f"\n**其他收入小計：{oth_sub}**\n\n"

inc_total = re.search(r'\*\*收入合計\*\*：([\d,]+)', content).group(1)
output += f"### **收入合計：{inc_total}**\n\n"

output += "#### 支出項目\n---\n**固定支出**\n"
output += generate_table(fixed_expense)
fix_sub = re.search(r'固定支出小計：([\d,]+)', content).group(1)
output += f"\n**固定支出小計：{fix_sub}**\n\n"

output += "**非固定支出**\n"
output += generate_table(variable_expense)
var_sub = re.search(r'非固定支出小計：([\d,]+)', content).group(1)
output += f"\n**非固定支出小計：{var_sub}**\n\n"

exp_total = re.search(r'\*\*支出合計\*\*：([\d,]+)', content).group(1)
output += f"### **支出合計：{exp_total}**\n\n"

output += "---\n### 財務總結\n\n| 項目 | 金額 |\n| --- | --- |\n"
for s in sums:
    output += f"| {s} | {summary_data.get(s, 'N/A')} |\n"

with open('output.md', 'w', encoding='utf-8') as f:
    f.write(output)

print("output.md generated successfully!")
