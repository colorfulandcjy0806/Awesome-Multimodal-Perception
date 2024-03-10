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
        '序号': 3,
        '类型': '3D目标检测',
        '论文名称': 'UniMODE: Unified Monocular 3D Object Detection',
        '作者': 'Zhuoling Li, Xiaogang Xu, SerNam Lim, Hengshuang Zhao',
        '发表单位': 'The University of Hong Kong、Zhejiang University、University of Central Florida',
        '期刊/会议': 'CVPR2024',
        '论文链接': 'https://arxiv.org/abs/2402.18573',
        '代码链接': 'https://arxiv.org/abs/2402.18573',
        '解读链接': 'https://zhuanlan.zhihu.com/p/686228362'
    }

    insert_paper_info(new_paper, "README.md")
    insert_paper_info(new_paper, "English.md")
