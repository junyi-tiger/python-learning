'''
方法论
    - 纵览Python计算生态，看见更大的世界
实践能力
    - 初步编写带有计算生态的复杂程序
'''
# 从数据处理到人工智能
# 数据表示->数据清洗->数据统计->数据可视化->数据挖掘->人工智能
# Python库之数据分析
'''
Numpy: 表达N维数组的最基础库
- Python接口使用，C语言实现，计算速度优异
- Python数据分析及科学计算的基础库，支撑Pandas等
- 提供最直接的矩阵运算、广播函数、线性代数等功能
Pandas: Python数据分析高层次应用库
- 提供了简单易用的数据结构和数据分析工具
- 理解数据类型与索引的关系，操作索引即操作数据
- Python最主要的数据分析功能库，基于Numpy开发
SciPy: 数学、科学和工程计算功能库
- 提供了一批数学算法及工程数据运算功能
- 类似Matlab，可用于如傅里叶变换、信号处理等应用
- Python最主要的科学计算功能库，基于Numpy开发
'''

# Python库之数据可视化
'''
Matplotlib: 高质量的二维数据可视化功能库
- 提供了超过100种数据可视化展示效果
- 通过matplotlib.pyplot子库调用各可视化效果
- Python最主要的数据可视化功能库，基于Numpy开发
Seaborn: 统计类数据可视化功能库
- 提供了一批高层次的统计类数据可视化展示效果
- 主要展示数据间分布、分类和线性关系等内容
- 基于Matplotlib开发，支持Numpy和Pandas
Mayavi: 三维科学数据可视化功能库
- 提供了一批简单易用的3D科学计算数据可视化展示效果
- 目前版本是Mayavi2，三维可视化最主要的第三方库
- 支持Numpy、TVTK、Envisage等第三方库
'''

# Python库之文本处理
'''
PyPDF2: 用来处理pdf文件的工具集
- 提供了一批处理PDF文件的计算功能
- 支持获取信息、分隔/整合文件、加密解密等
- 完全Python语言实现，不需要额外依赖，功能稳定
NLTK: 自然语言文本处理第三方库
- 提供了一批简单易用的自然语言文本处理功能
- 支持语言文本分类、标记、语法句法、语义分析等
- 目前最优秀的Python自然语言处理库
Python-docx: 创建 或更新Microsoft Word文件的第三方库
- 提供创建或更新.doc .docx等文件的计算功能
- 增加并配置段落、图片、表格、文字等，功能全面
'''

# Python库之机器学习
'''
Scikit-learn: 机器学习方法工具集
- 提供一批统一化的机器学习方法功能接口
- 提供聚类、分类、回归、强化学习等计算功能
- 机器学习最基本且最优秀的第三方库
TensorFlow: AlphaGo背后的机器学习计算框架
- 谷歌公司推动的开源机器学习框架
- 将数据流图作为基础，图节点代表运算，边代表张量
- 应用机器学习方法的一种方式，支持谷歌人工智能应用
MXNet: 基于神经网络的深度学习计算框架
- 提供可拓展的神经网络及深度学习计算功能
- 可用于自动驾驶、机器翻译、语音识别等众多领域
- Python最重要的深度学习计算框架
'''