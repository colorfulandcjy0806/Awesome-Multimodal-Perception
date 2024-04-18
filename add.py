# 文件名: add_paper_to_markdown.py
def insert_paper_info(entry, filepath):
    """
    在Markdown文件的表格中插入新的论文信息。
    
    参数:
    - entry: 包含论文信息的字典
    - filepath: Markdown文件的路径
    """
    end_of_table_marker = "| ...  | ...             | ...                                                          | ...                                                          | ...                              | ...                 | ...                                   | ...                                                | ...                                         |"
    new_line = f"| {entry['序号']} | {entry['类型']} | {entry['论文名称']} | {entry['作者']} | {entry['发表单位']} | {entry['期刊/会议']} | [📄]({entry['论文链接']}) | [💻]({entry['代码链接']}) | [🔍]({entry['解读链接']}) |\n"
    
    with open(filepath, 'r') as file:
        lines = file.readlines()
    
    # Find the end of the table and insert new entry before it
    for i, line in enumerate(lines):
        if line.strip() == end_of_table_marker.strip():
            # Insert the new line before the end of table marker
            lines.insert(i, new_line)
            break
    
    with open(filepath, 'w') as file:
        file.writelines(lines)

if __name__ == "__main__":
    # 示例论文条目
    new_paper = {
        '序号': 9,
        '类型': '相机+激光雷达融合',
        '论文名称': "BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird's-Eye View Representation",
        '作者': 'Zhijian Liu, Haotian Tang, Alexander Amini, Xinyu Yang, Huizi Mao, Daniela Rus, Song Han',
        '发表单位': 'MIT、上海交通大学',
        '期刊/会议': 'ICRA 2023',
        '论文链接': 'https://arxiv.org/abs/2205.13542',
        '代码链接': 'https://github.com/mit-han-lab/bevfusion',
        '解读链接': 'https://zhuanlan.zhihu.com/p/692741500'
    }

    insert_paper_info(new_paper, "README.md")
    insert_paper_info(new_paper, "English.md")
