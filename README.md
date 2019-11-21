# Isolation-Froest2
Anomaly detection.As a "simple ml" for "beginner"

项目背景-Background
=====

这个项目是延续上一个<a href="https://github.com/SilenceSengoku/IsolationForest">IFroest</a>
的项目。同样是主张实战。

网络上很多资料都是以随机数据集做测试，这其实对很多初学者很不友好。也包括我初学的时候。

所以，我认为应该有比较好的一份实战示例供初学者练习经验，

而不是在一次次失败的在coding和bug中逐渐地被劝退。

更多的感慨留在知乎文章一并发表。

数据集-Dataset
=====
我不会说明我的数据集customers_nums.csv的来源，

我只能告诉你cr和7cr这两列数据都是我以某种方法提取的特征。

虽然这可能会感觉和网络上的其他资料一样晕乎，但是对特征的概念你可以先暂缓了解。

初学者最需要做的：
是先尝试跑通示例代码，
理解代码各个部分分工，
最后再去思考提取特征等问题，
并尝试彻底解决某种实际问题。


参数-paramete
=====
> n_estimators : int, optional (default=100) 

 设置itree 数量 
 
> max_samples : int or float, optional (default=”auto”)

样本抽取比例、或样本全部数量

> contamination : float in (0., 0.5), optional (default=0.1)

设置样本中异常点的比例

> max_features : int or float, optional (default=1.0)

提取特征比例、或特征全部个数。

安装-Install
=====
my python version is 3.6.5
你需要/You need:

pandas，numpy，sklearn，matplotlib，scipy

> pip install pandas

> pip install numpy

> pip install sklearn

> pip install scipy

> pip install matplotlib



作者-Author & Maintainers
=====
<a href="https://github.com/SilenceSengoku">@Sengoku·Crow·Lu</a>

<a href="https://www.zhihu.com/people/firesnake-67/activities">Sengoku·Crow·Lu's zhihu</a>

Public statement:

this is Author statement.

No reprint without authorization.Thank you for your cooperation.


参考-Reference
=====
<a href="https://cs.nju.edu.cn/zhouzh/zhouzh.files/publication/icdm08b.pdf">Isolation Forest</a>
by Fei Tony Liu, Kai Ming TingGippsland School of Information TechnologyMonash University, Victoria, Australia,2008

<a href="https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/ensemble/_iforest.py">github’s iforest_ source code</a> by https://scikit-learn.org

<a href="https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest">Sklearn' Isolation Forest Parameter introduction</a>

<a href="https://sklearn.apachecn.org/docs/0.21.3/26.html">Sklearn 中文档</a>

<a href="https://www.zhihu.com/people/firesnake-67/activities">iForest （Isolation Forest）孤立森林</a>by YeZhu - 2017

<a href="https://blog.csdn.net/aiyinsimei/article/details/48003859#0-tsina-1-5960-397232819ff9a47a7b7e80a40613cfe1">Isolation forest的python代码实现</a> by 明日菜心_CSDN 2015-08

<a href="https://blog.csdn.net/ye1215172385/article/details/79762317">IForest主要参数和函数介绍</a>by 夕阳下江堤上的男孩_CSDN 2018-03

