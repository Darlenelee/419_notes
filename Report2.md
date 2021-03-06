# Report 2

> Requirements:
>
> Write a technical report about CPU, Memory, Storage(Ceph), Network and xPU  
> - Vendors or types or technologies
>   - Features
>   - Pros & Cons
> - Key indicators
>   - What, how to measure, scope
> - Your own comment
>   - For example
>     - How to tradeoff

---
# Memory #
## 简介 ##
术语“Memory”适用于能够临时存储数据的任何电子组件。我们在这里主要关心两种Memory:
- INTERNAL memory  
    - 程序运行时暂时记忆数据。内部存储器使用微导体，即快速专用电子电路。内部存储器对应于我们称之为随机存取存储器（RAM）的内存。

- AUXILIARY memory
    -（也称为物理内存或外部存储器），用于长期存储信息，包括在计算机关闭后。辅助存储器对应于诸如硬盘驱动器的磁存储设备，诸如CD-ROM和DVD-ROM的光存储设备，以及只读存储器。

## 性能参数 ##
- 存储速度
    - 内存的存储速度用存取一次数据的时间来表示，单位为纳秒，记为ns，1秒=10亿纳秒，即1纳秒=10ˉ9秒。Ns值越小，表明存取时间越短，速度就越快。目前，DDR内存的存取时间一般为6ns，而更快的存储器多用在显卡的显存上，如：5ns、 4ns、 3.6ns、 3.3ns、 2.8ns、 等
 - 存储容量
    - 表示存储器可以存储的全局信息量（以位为单位）
- 内存带宽
    - 从内存的功能上来看，我们可以将内存看作是内存控制器（一般位于北桥芯片中）与CPU之间的桥梁或仓库。显然，内存的存储容量决定“仓库”的大小，而内存的带决定“桥梁的宽窄”，两者缺一不可。 提示：内存带宽的确定方式为：B表示带宽、F表于存储器时钟频率、D表示存储器数据总线位数，则带宽B=F*D/8

- CL
    - CL是CAS Lstency的缩写，即CAS延迟时间，是指内存纵向地址脉冲的反应时间，是在一定频率下衡量不同规范内存的重要标志之一。对于PC1600和PC2100的内存来说，其规定的CL应该为2，即他读取数据的延迟时间是两个时钟周期。也就是说他必须在CL=2R 情况下稳寰工作的其工作频率中。

- SPD芯片
    - SPD是一个8针256字节的EERROM(可电擦写可编程只读存储器) 芯片.位置一般处在内存条正面的右侧, 里面记录了诸如内存的速度、容量、电压与行、列地址、带宽等参数信息。当开机时，计算机的BIOS将自动读取SPD中记录的信息。
- 奇偶校验
    - 奇偶校验就是内存每一个字节外又额外增加了一位作为错误检测之用。当CPU返回读顾储存的数据时，他会再次相加前8位中存储的数据，计算结果是否与校验相一致。当CPU发现二者不同时就会自动处理。
- 吞吐量
    - 它定义了每单位时间交换的信息量，以每秒位数表示
-  非易失性
    - 非易失性，表征存储器在没有电力供应时存储数据的能力

## 内存的主要厂商 ##
- Corsair
    - 海盗船内存（Corsair Memory），国内又称海盗旗，Corsair成立于1994年,由Don Lieberman、John Beekley与Andy Paul创立。是一家位于加利福尼亚州佛利蒙的私有公司。
- G.Skill
    - 品牌简介：芝奇成立于1989年，由一群IT爱好者共同创立于台湾。G.Skill以不断推陈出新并持续研发出高超频性能产品，短时间内即于内存产业展露头角，为满足市场需求及商业竞争力，并提供极具竞争力的价格，更保证产品高规质量以及完善售后服务，因此短短数年间，名声已响彻全球五大洲、横跨超过70个国家的计算机玩家族群。
- Micron
    - 镁光科技有限公司（Micron Technology, Inc.）是高级半导体解决方案的全球领先供应商之一。Micron通过全球化的运营，镁光公司制造并向市场推出DRAM、NAND闪存、CMOS图像传感器、其它半导体组件以及存储器模块，用于前沿计算、消费品、网络和移动便携产品。美光公司普通股代码为MU，在纽约证券交易所交易（NYSE）。
- OCZ
    - 总部位于加州圣荷西的OCZ技术团队成立于2002年，专精于高速内存领域，已成为制造与销售固态硬盘（solid state drive, SSD）的主流供货商，这种插断性技术正逐渐取代传统的旋转式磁性硬盘（hard disk drive, HDD），改变市场游戏规则。SSD的速度较快，可靠度较好，运行温度较低，且消耗的功率较目前大多数计算机所使用的HDD明显较少。除了SSD技术，OCZ还提供用于运算装置与系统的高性能组件，包括企业级功率管理产品，以及先进的计算机游戏解决方案。
- Mushkin
    - Mushkin（/mʊʃkɪn/）是一家以生产计算机内存模块（RAM）而闻名的公司，位于德克萨斯州的Pflugerville。其客户包括游戏玩家和行业专业人士。它声称拥有Apple Inc.和NASA。 Mushkin产品包括计算机电源单元（PSU），以及用于台式机，服务器和笔记本电脑的RAM模块。他们还生产一系列USB闪存驱动器和固态驱动器SSD。他们的存储器产品有几种性能类别，从标准到极端。其中一个值得注意的[需要引用] RAM产品是“REDLINE”系列，专为超频玩家设计。
- Kingston
- Hynix
    - Hynix 海力士芯片生产商，源于韩国品牌英文缩写"HY"。海力士即原现代内存，2001年更名为海力士。海力士半导体是世界第三大DRAM制造商，也在整个半导体公司中占第九位。
- Samsung
- Lenovo

### 外储的主要厂商 ###
- Western Digital
    - Western Digital是世界上最大和最着名的计算机硬盘制造商之一。 Western Digital提供各种存储和效率功能的外置硬盘。除了西部数据的硬盘驱动器的一些高端功能，如更快的数据传输，更高的容量，一流的质量和可靠性等等，Western Digital品牌的硬盘驱动器也以一些创新功能而闻名。这些可能包括使用高级算法的额外安全措施，如果数据存储在这些硬盘中，则可确保安全性。西部数据的硬盘驱动器有各种尺寸选项，如500 GB，1 TB，2 TB，3 TB甚至更多。Western Digital的最新硬盘系列还配备了先进的数据备份软件。这可确保最安全地备份硬盘驱动器上的数据。因此，您的数据可以免受各种损害或恶意软件的侵害。这些功能使Western Digital成为硬盘的最佳品牌之一。
-  Seagate Technology
    - 希捷.这是一家位于美国的着名数据存储公司。希捷开发了其首款HDD（硬盘驱动器），这是一款5.25英寸硬盘，1980年的初始存储容量为5兆字节。希捷是制造最可靠硬盘的领先品牌。世界上出色的数据存储解决方案。它一直在开发出色的数字产品，使全球的个人和组织能够创建，共享和保留最关键的业务数据。凭借其高端智能硬盘系列，希捷科技一直在抓住技术市场。它不时推出新的和创新的硬盘驱动器，它们具有惊人的技术规格，方便用户使用。希捷科技的硬盘驱动器的一些显着特性包括更大的存储容量，更好的传输速率，增强的性能，安全的备份和整体安全性，以及更多优化用户的整体体验。
-  Hitachi
    - 即使在硬盘系列中，日立也因其制造和提供一些性能最佳，最可靠的硬盘驱动器而享誉全球。在技​​术规格方面，日立不亚于任何其他品牌。它的所有硬盘都具有更高的数据存储容量，更好的数据传输速率，增强的安全级别，用于保持数据安全的优化备份软件等等。日立硬盘的最佳功能之一是，与其他品牌的硬盘相比，日立提供的硬盘非常实惠。您可以通过Hitachi获得与特定硬盘相同的技术规格，价格低于其他同类品牌。这就是为什么日立在那里排名最好和最便宜的硬盘的原因。如果您正在为您的系统寻找一些高质量，可靠但价格合理的硬盘，那么您可以购买日立品牌的硬盘。
- Toshiba
    - 东芝提供全系列不同类型的硬盘驱动器，包括外部硬盘驱动器，内置硬盘驱动器，SSD等，以便为用户提供优化的存储体验。在为您的系统购买最可靠，最高效的硬盘时，东芝是一个能够确保各方面性能最佳的品牌。您可以选择东芝的各种高性能硬盘，这些硬盘以其出色的功能和技术规格而着称。您是否正在寻求更高的存储容量或更好的数据传输速率和速度，安全存储重要数据，正确备份为保证数据安全和其他高端功能，东芝提供坚如磐石的高品质，可靠性以及急需的专业知识，帮助您加快硬盘的升级。
- HGST
    - HGST致力于为全球个人提供高度创新，移动，高价值的数据中心，个人以及消费者电子数据存储解决方案。 HGST以为全球一些最大，最复杂的企业，OEM和超大规模云客户提供高端存储基础设施而闻名。HGST品牌的硬盘在高品质和可靠性方面享有无与伦比的声誉。 HGST的这些硬盘以提供高度优化的数据存储和备份软件以及高度创新和高质量的硬盘驱动器组合而闻名，用于存储，管理和保护各种数据。
## 为Server挑选内存--TradeOff ##
- How much server memory do you really need? 
    - 这可能是确定应用程序的最佳服务器选项时要问的第一个问题，遗憾的是没有直截了当的答案。由于在现代商业中使用多种服务器，因此可提供大量的解决方案。服务器支持的用户数量与可持续性所需的内存量之间的关系很高。在服务器使用户不断超过内存容量的情况下，将遇到性能复杂性，其中所述服务器将从驱动器存储器访问虚拟内存并且操作速度慢得多。与往常一样，研究是确定哪些选项最适合您的应用的关键。定义访问服务器的大量用户以及将被利用和访问的程序和文件类型是一个重要的起点，以便最好地确定服务器内存的基本要求。提前计划未来的扩展，以便保持高水平的一致性操作，因为增加的用户将随着时间的推移而降低性能。
- What are other companies buying?
    - 如前所述，服务器内存使用的基线因应用程序而异。随着日益发展的技术不断发展，8 GB DIMM在2年前广泛应用于服务器中。但是，随着大容量DIMM的价格随着时间的推移而降低，1TB DIMM可用，为用户提供更大的灵活性，同时提高生产力和增长空间。 Premio的可定制服务器产品解决方案为各种用户类型和应用程序大小提供了卓越的性能和价值，其中包括Scalestream服务器阵容中的云计算解决方案的高密度服务器。 OmniStream产品系列提供可调节性和性能的通用服务器，DuraStream型号面向任务关键型应用。 Flachestream系列提供市场上速度最快，密度最高的机架式服务器，吞吐量为20GB / s。
- Should you fill every slot in the server?
    - 根据所选解决方案的使用要求，这会有所不同。由于目前高容量存储器选项的成本较低，人们不会想到。但是，有许多解决方案，更大的内存大小提供了竞争性的业务优势。对许多数据中心管理员来说，平衡性能和容量是一项持续的困难，因为向服务器添加内存库会降低其运行速度。这里要考虑的是，在将内存库添加到服务器之前，考虑已安装的内存并了解特定用例的需求是非常重要的。也可以在服务器中组合DIMM容量大小，但最好建议保持类似的大小，例如8GB和16GB。可能不支持使用大于16GB的DIMM，可能不建议使用。
- How much memory and disk space will your server need?
    - 用户对服务器施加的不同压力水平直接与服务器及其指定角色的责任相关。关于存储数量，该值可能会根据其整体作业在同一数据中心内从一台服务器到下一台服务器发生变化。如前所述，内存容量还与服务器预期的可访问性级别以及用户将访问的文件和程序类型有关。在选择适当的存储设备时，虚拟化数据中心为内存分配创造了一个强大的优先级
## Comment ##
Web服务器内存的选择标准主要根据网站的流量而定，对于一般的企业站或者小型网站，服务器的内存通常选择较小的就可以了，但是随着网站流量的增加，建议将网站升级到，才能够满足访问量上万的需求。对于服务器来说，内存的大小可根据实际应用来决定。
# xPU Report #

现如今， 各种计算单元层出不穷，他们大多都以xPU（Processing unit）的方式命名，其中除了最为我们所熟知的CPU与GPU之外，还有 TPU, NPU，DPU等等，我们下面就分别来简单报告一下它们的具体情况。

---

## CPU ##
### 简介
中央处理器 （Central Processing Unit，CPU），是计算机的主要设备之一，功能主要是解释计算机指令以及处理计算机软件中的数据。计算机的可编程性主要是指对中央处理器的编程。1970年代以前，中央处理器由多个独立单元构成，后来发展出由集成电路制造的中央处理器，這些高度收縮的元件就是所謂的微处理器，其中分出的中央处理器最為复杂的电路可以做成单一微小功能强大的单元。

中央处理器主要包括运算器（算术逻辑运算单元，ALU，Arithmetic Logic Unit）和高速缓冲存储器（Cache）及实现它们之间联系的数据（Data）、控制及状态的总线（Bus）。它与内部存储器（Memory）和输入/输出（I/O）设备合称为电子计算机三大核心部件。

简单来说就是：计算单元、控制单元和存储单元，架构如下图所示：

![此处输入图片的描述][1]

其中，如下图所示，计算单元主要执行算术运算、移位等操作以及地址运算和转换；存储单元主要用于保存运算中产生的数据以及指令等；控制单元则对指令译码，并且发出为完成每条指令所要执行的各个操作的控制信号。

![此处输入图片的描述][2]

### 性能参数
#### 主频
主频也叫时钟频率，单位是兆赫（MHz）或千兆赫（GHz），用来表示CPU的运算、处理数据的速度。
#### 外频
外频是CPU的基准频率，单位是MHz。CPU的外频决定着整块主板的运行速度。
#### 总线频率
前端总线（FSB)是将CPU连接到北桥芯片的总线。前端总线（FSB）频率（即总线频率）是直接影响CPU与内存直接数据交换速度。
#### 倍频系数
倍频系数是指CPU主频与外频之间的相对比例关系。在相同的外频下，倍频越高CPU的频率也越高。
#### 缓存
缓存大小也是CPU的重要指标之一，而且缓存的结构和大小对CPU速度的影响非常大，CPU内缓存的运行频率极高，一般是和处理器同频运作，工作效率远远大于系统内存和硬盘。具体又分为L1/L2/L3三层。

### 厂商 ###
#### 1.Intel公司 ####
Intel是生产CPU的老大哥，它占有大约80%的市场份额，Intel生产的CPU就成了事实上的x86CPU技术规范和标准。

#### 2·AMD公司 ####
除了Intel公司外，最有力的挑战的就是AMD公司。AMD公司专门为计算机、通信和消费电子行业设计和制造各种创新的微处理器（CPU、GPU、APU、主板芯片组、电视卡芯片等)、闪存和低功率处理器解决方案
#### 3·Cyrix ####
曾经风靡一时的世界第三大CPU生产厂家，现在被VIA与AMD分别收购生产线与技术。
#### 4·IBM公司 ####
国际商业机器公司IBM，拥有了自己的芯片生产线，主要生产服务器用POWER处理器。

---
## GPU ##
### 简介 ###
图形处理器（英语：Graphics Processing Unit，缩写：GPU），又称显示核心、视觉处理器、显示芯片，是一种专门在个人电脑、工作站、游戏机和一些移动设备（如平板电脑、智能手机等）上图像运算工作的微处理器。

用途是将计算机系统所需要的显示信息进行转换驱动，并向显示器提供行扫描信号，控制显示器的正确显示，是连接显示器和个人电脑主板的重要元件，也是“人机对话”的重要设备之一。显卡作为电脑主机里的一个重要组成部分，承担输出显示图形的任务，对于从事专业图形设计的人来说显卡非常重要。

工作原理上简单地说，GPU就是能够从硬件上支持T&L（Transform and Lighting，多边形转换和光源处理）的显示芯片，由于T&L是3D渲染中的一个重要部分，其作用是计算多边形的3D位置与处理动态光线效果，也能称为“几何处理”。一个好的T&L单元，能提供细致的3D物体和高级的光线特效；只不过大多数PC中，T&L的大部分运算是交由CPU处理的(这就也就是所谓软件T&L)，因为CPU的任务繁多，除了T&L之外，还要做内存管理和输入响应等非3D图形处理工作，所以在实际运算的时候性能会大打折扣，一般出现显卡等待CPU数据的情况，CPU运算速度远跟不上时下复杂三维游戏的要求。即使CPU的工作频率超出1GHz或更高，对它的帮助也不大，因为这是PC本身设计造成的问题，与CPU的速度无太大关系。

为什么GPU特别擅长处理图像数据呢？这是因为图像上的每一个像素点都有被处理的需要，而且每个像素点处理的过程和方式都十分相似，也就成了GPU的天然温床。

GPU简单架构如下图所示：

![此处输入图片的描述][3]

但有一点需要强调，虽然GPU是为了图像处理而生的，但是我们通过前面的介绍可以发现，它在结构上并没有专门为图像服务的部件，只是对CPU的结构进行了优化与调整，所以现在GPU不仅可以在图像处理领域大显身手，它还被用来科学计算、密码破解、数值分析，海量数据处理（排序，Map-Reduce等），金融分析等需要大规模并行计算的领域。

所以GPU也可以认为是一种较通用的芯片。
### 类型 ###
#### 独立显卡 ####
显卡是通过PCI-Express、PCI或AGP等扩展槽界面与主板连接的，而通常它们可以相对容易地被取代或升级（假设主板能支持升级）。现在，仍然有少数显卡采用带宽有限的PCI插槽作连接，但它们通常只会在主板没有提供PCI-Express和AGP插槽的情况下才会使用。
在现今的定义里，独立绘图处理器不一定需要，是可以被移除的，也不一定要直接与主板连接。所谓的“专用”即是指独立显卡（或称专用显卡）内的RAM只会被该卡专用，而不是指显卡是否可从主板上独立移除。基于体积和重量的限制，供笔记本电脑使用的独立绘图处理器通常会通过非标准或独特的接口作连接。然而，由于逻辑接口相同，这些端口仍会被视为PCI-Express或AGP，即使它们在物理上是不可与其他显卡互换的。
一些特别的技术，如NVIDIA的SLI和ATI的CrossFire允许多个绘图处理器共同处理一个单一的视频输出，可令电脑的图像处理能力增加。
#### 集成绘图处理器 ####
集成绘图处理器（或称内置显示核心）是设在主板或CPU上的绘图处理器，运作时会借用电脑内部分的系统存储器。2007年装设集成显示的个人电脑约占总出货量的90%，相比起使用独立显卡的方案，这种方案可能较为便宜，但性能也许相对较低。从前，集成绘图处理器往往会被认为是不适合于运行3D游戏或精密的图形型运算。然而，如Intel GMA X3000（Intel G965 芯片组）、AMD的Radeon HD 4290（AMD 890GX 芯片组）和NVIDIA的GeForce 8200（NVIDIAnForce 730a芯片组）已有能力处理对系统需求不是太高的3D图像。当时较旧的集成图形处理器组缺乏如硬件T&L等功能，只有较新型号才会包含。
影响集成绘图处理器的性能，其中一个原因是由于内置显示核心的运算速度。同时，图形处理器在运作时会消耗一定数量的存储器。系统存储器的速度比高级独立绘图存储器来得慢，系统存储器的发送速度可能是10GB/s至20GB/s左右，独立绘图存储器则至少有50GB/s，甚至超过150GB/s，取决于型号而定。
不过从2009年开始，图形处理器已经从主板移去处理器了，如Intel的Westmere架构至目前的Kaby Lake架构。不过极致版并没有集成图形处理器。集成至处理器的好处是由于绘图及处理器芯片工艺为相同(Westmere除外，CPU为32nm而GPU为45nm)，可以减低热功耗。随着内显技术的成熟，目前的内显已经足够应付基本3D的需求，不过仍然依赖主板本身的存储器。

### 性能指标 ###
#### 显存位宽 ####
指一个时钟周期内能传输数据的位数。主流256 bit 和 512 bit。

#### 显存类型 ####
和电脑的运行内存一样，主流为DDR3与DDR5。

#### 显存带宽 ####
指每秒能传输的数据量。 
显存带宽=显存频率X显存带宽/8/1000 (GB/s) 
eg: GeForce GTX 1060 显存频率8008MHz，显示位宽192bit 
则：显存带宽=8008X192/8/1000(GB/s)=192.2 GB/s
#### 显存频率 ####
指默认情况下显存在显卡上的工作频率，厂商设定的工作频率一般比最大频率小。
#### 显存容量 ####
用来存储显卡芯片即将处理和处理完的数据，对显卡性能影响较小，当容量大于GPU的性能时多余的容量是浪费。
#### 核心频率 ####
GPU的运算频率，与计算机的主频差不多。
#### shader 频率 ####
即着色器频率，它是DirectX 10统一渲染架构（Unified Shader Architecture）诞生后出现的新产物。
#### 制作工艺 ####
制作工艺指的是晶体管与晶体管之间的距离，制作工艺越小说明集成度越高，只会影响到功耗，对性能并没有影响。


### 厂商 ###
#### 英特尔 ####
英特尔的GPU基本为集成显卡芯片，用于英特尔的主板和英特尔的CPU。可能你想不到，要是只按市场占有率计算，英特尔随着他主板及CPU发售的集成GPU占据了整个GPU市场的60%以上。
他的GPU主要有：唯一一款独立显卡芯片Intel 740（i740）。Extreme Graphics系列、GMA系列（集成于芯片组中）。现在的HD Graphics系列 [1]  、Iris™ Graphics系列 [2]  、Iris™ Pro Graphics [2]  系列等（集成于CPU中）。
#### NVIDIA ####
NVIDIA是现在最大的独立显卡芯片生产销售商。
他的GPU包括大家熟悉的Geforce系列 [3]  ，包括GTX、GTS、GT等。专业工作站的Quadro系列 [4]  ，超级计算的Tesla系列 [5]  ，多显示器商用的NVS系列 [6]  ，移动设备的Tegra系列 [7]  。
以前也销售集成在主板上的集成显卡芯片，这些随着主板芯片组一起发售，但是由于AMD收购ATI后自身主板芯片组GPU能力提高，NVIDIA芯片组如日中天的景象已经消失了。
曾经为游戏机Xbox、PS3供应GPU。
#### AMD(ATI) ####
AMD是世界上第二大的独立显卡芯片生产销售商，他的前身就是ATI，2006年AMD以54亿美元收购ATI。
他的GPU主要是大家熟悉的Radeon系列 [8]  ，包括以前的X、HD系列，近几年的R9、R7、R5、R3，现在的RX系列等。专业工作站的FireGL系列，超级计算的FireStream系列，多显示器商用的FireMV系列，现在前三者已合并为FirePro系列 [9]  。
早期ATI还生产过Wonder系列、Mach系列、Rage系列芯片。
除了独立显卡之外AMD还拥有集成显卡芯片，集成于芯片组、APU中。
由于AMD收购ATI后，其主板市场迅速扩大，已经夺取了NVIDIA在AMD处理器主板芯片组的半壁江山。
就现在的发售量和发售盈利方面，AMD的GPU市场占有率方面仍然略输于NVIDIA。
AMD也是游戏机Xbox 360、Wii、Wii U、PS4、Xbox One的GPU供应商。

---

## TPU ##
### 简介 ###
TPU，是Tensor Processing Unit的简称，是谷歌打造的处理器，是专为机器学习量身定做的，执行每个操作所需的晶体管数量更少，自然效率更高。

原来很多的机器学习以及图像处理算法大部分都跑在GPU与FPGA（半定制化芯片）上面，但这两种芯片都还是一种通用性芯片，所以在效能与功耗上还是不能更紧密的适配机器学习算法，而且Google一直坚信伟大的软件将在伟大的硬件的帮助下更加大放异彩，所以Google便想，我们可不可以做出一款专用机机器学习算法的专用芯片，TPU便诞生了。

据称，TPU与同期的CPU和GPU相比，可以提供15-30倍的性能提升，以及30-80倍的效率（性能/瓦特）提升。初代的TPU只能做推理，要依靠Google云来实时收集数据并产生结果，而训练过程还需要额外的资源；而第二代TPU既可以用于训练神经网络，又可以用于推理。

![此处输入图片的描述][4]
谷歌第二代TPU

![此处输入图片的描述][5]
TPU 各模块的框图

![此处输入图片的描述][6]
TPU芯片布局图

如上图所示，TPU在芯片上使用了高达24MB的局部内存，6MB的累加器内存以及用于与主控处理器进行对接的内存，总共占芯片面积的37%（图中蓝色部分）。

这表示谷歌充分意识到了片外内存访问是GPU能效比低的罪魁祸首，因此不惜成本的在芯片上放了巨大的内存。相比之下，英伟达同时期的K80只有8MB的片上内存，因此需要不断地去访问片外DRAM。

另外，TPU的高性能还来源于对于低运算精度的容忍。研究结果表明，低精度运算带来的算法准确率损失很小，但是在硬件实现上却可以带来巨大的便利，包括功耗更低、速度更快、占芯片面积更小的运算单元、更小的内存带宽需求等...TPU采用了8比特的低精度运算。

---
## NPU ##
### 简介 ###
NPU（Neural network Processing Unit）， 即神经网络处理器。也是针对神经网络来特别开发的处理器。神经网络中存储和处理是一体化的，都是通过突触权重来体现。而冯·诺伊曼结构中，存储和处理是分离的，分别由存储器和运算器来实现，二者之间存在巨大的差异。当用现有的基于冯·诺伊曼结构的经典计算机（如X86处理器和英伟达GPU）来跑神经网络应用时，就不可避免地受到存储和处理分离式结构的制约，因而影响效率。这也就是专门针对人工智能的专业芯片能够对传统芯片有一定先天优势的原因之一。

### 代表 ###
NPU的典型代表有国内的寒武纪芯片和IBM的TrueNorth。以中国的寒武纪为例，DianNaoYu指令直接面对大规模神经元和突触的处理，一条指令即可完成一组神经元的处理，并对神经元和突触数据在芯片上的传输提供了一系列专门的支持。

用数字来说话，CPU、GPU与NPU相比，会有百倍以上的性能或能耗比差距——以寒武纪团队过去和Inria联合发表的DianNao论文为例——DianNao为单核处理器，主频为0.98GHz，峰值性能达每秒4520亿次神经网络基本运算，65nm工艺下功耗为0.485W，面积3.02平方毫米mm。

### 备注 ###
中星微电子（Vimicro）的星光智能一号。中星微于2016年抢先发布了“星光智能一号”NPU。但是，这不是一个专为加速Neural Network而开发的处理器。虽说对外号称是NPU，但其实只是DSP，仅支持网络正向运算，无法支持神经网络训练。业内都知道其内部集成了多个DSP核（其称为NPU core），通过SIMD指令的调度来实现对CNN、DNN的支持。以这个逻辑，似乎很多芯片都可以叫NPU，其他以DSP为计算核心的SOC芯片的命名和宣传都相对保守了。

---

## 其他 ##
BPU -- Brain Processing Unit，
是由地平线科技提出的嵌入式人工智能处理器架构。第一代是高斯架构，第二代是伯努利架构，第三代是贝叶斯架构。目前地平线已经设计出了第一代高斯架构，并与英特尔在2017年CES展会上联合推出了ADAS系统（高级驾驶辅助系统）。

DPU -- Deep learning Processing Unit, 即深度学习处理器）最早由国内深鉴科技提出，基于Xilinx可重构特性的FPGA芯片，设计专用的深度学习处理单元（可基于已有的逻辑单元，设计并行高效的乘法器及逻辑电路，属于IP范畴），且抽象出定制化的指令集和编译器（而非使用OpenCL），从而实现快速的开发与产品迭代。事实上，深鉴提出的DPU属于半定制化的FPGA。

Dataflow Processing Unit。数据流处理器。创立于2010年的wave computing公司将其开发的深度学习加速处理器称为Dataflow Processing Unit(DPU)，应用于数据中心。Wave的DPU内集成1024个cluster。每个Cluster对应一个独立的全定制版图，每个Cluster内包含8个算术单元和16个PE。其中，PE用异步逻辑设计实现，没有时钟信号，由数据流驱动，这就是其称为Dataflow Processor的缘由。使用TSMC 16nm FinFET工艺，DPU die面积大概400mm^2，内部单口sram至少24MB，功耗约为200W，等效频率可达10GHz，性能可达181TOPS。前面写过一篇他家DPU的分析，见传输门AI芯片|浅析Yann LeCun提到的两款Dataflow Chip。

APU -- Accelerated Processing Unit, 加速处理器，AMD公司推出加速图像处理芯片产品。

BPU -- Brain Processing Unit, 地平线公司主导的嵌入式处理器架构。

EPU -- Emotion Processing Unit，
Emoshape 并不是这两年才推出EPU的，号称是全球首款情绪合成（emotion synthesis）引擎，可以让机器人具有情绪。但是，从官方渠道消息看，EPU本身并不复杂，也不需要做任务量巨大的神经网络计算，是基于MCU的芯片。结合应用API以及云端的增强学习算法，EPU可以让机器能够在情绪上了解它们所读或所看的内容。结合自然语言生成(NLG)及WaveNet技术，可以让机器个性化的表达各种情绪。例如，一部能够朗读的Kindle，其语音将根据所读的内容充满不同的情绪状态。

FPU -- Floating Processing Unit 浮点计算单元，通用处理器中的浮点运算模块。

HPU -- Holographics Processing Unit 全息图像处理器， 微软出品的全息计算芯片与设备。

IPU -- Intelligence Processing Unit， Deep Mind投资的Graphcore公司出品的AI处理器产品。

MPU/MCU -- Microprocessor/Micro controller Unit， 微处理器/微控制器，一般用于低计算应用的RISC计算机体系架构产品，如ARM-M系列处理器。


QPU -- Quantum Processing Unit。量子处理器。量子计算机也是近几年比较火的研究方向。作者承认在这方面所知甚少。可以关注这家成立于1999年的公司D-Wave System。DWave大概每两年可以将其QPU上的量子位个数翻倍一次。

RPU -- 
Radio Processing Unit, 无线电处理器， Imagination Technologies 公司推出的集合集Wifi/蓝牙/FM/处理器为单片的处理器。

Resistive Processing Unit。阻抗处理单元RPU。这是IBM Watson Research Center的研究人员提出的概念，真的是个处理单元，而不是处理器。RPU可以同时实现存储和计算。利用RPU阵列，IBM研究人员可以实现80TOPS/s/W的性能。

Ray-tracing Processing Unit。光线追踪处理器。Ray tracing是计算机图形学中的一种渲染算法，RPU是为加速其中的数据计算而开发的加速器。现在这些计算都是GPU的事情了。

SPU -- Streaming Processing Unit， 流处理器。流处理器的概念比较早了，是用于处理视频数据流的单元，一开始出现在显卡芯片的结构里。可以说，GPU就是一种流处理器。甚至，还曾经存在过一家名字为“Streaming Processor Inc”的公司，2004年创立，2009年，随着创始人兼董事长被挖去NVIDIA当首席科学家，SPI关闭。

TPU -- Tensor Processing Unit 张量处理器， Google 公司推出的加速人工智能算法的专用处理器。目前一代TPU面向Inference，二代面向训练。

VPU -- Vector Processing Unit 矢量处理器，Intel收购的Movidius公司推出的图像处理与人工智能的专用芯片的加速计算核心。

WPU -- Wearable Processing Unit， 可穿戴处理器，Ineda Systems公司推出的可穿戴片上系统产品，包含GPU/MIPS CPU等IP。

XPU -- 百度与Xilinx公司在2017年Hotchips大会上发布的FPGA智能云加速，含256核。

ZPU -- Zylin Processing Unit, 由挪威Zylin 公司推出的一款32位开源处理器。

---

## 总结 ##

总得来说，各种处理器，尤其是最新一段时间新发展出现的处理器大多都是根据具体使用需求和场景而特别定制开发的。不同的处理器有各自最为擅长的领域，我们应当根据实际情况来选择处理器。但同时也要注意有部分新处理器并没有很多的开创性和优势，噱头大于实用性，所以也不应当盲目迷信新处理器。

---
## 参考资料： ##
http://news.ifeng.com/a/20170830/51808889_0.shtml 

https://www.sohu.com/a/200698604_160923 

Wikipedia，Baidupedia


[1]: http://5b0988e595225.cdn.sohucs.com/images/20171028/e664ed39638648469655f0fefe19f731.png
[2]: http://5b0988e595225.cdn.sohucs.com/images/20171028/636a564e61c140bbbf2826cc9cbca527.jpeg
[3]: http://5b0988e595225.cdn.sohucs.com/images/20171028/e7ac26fc862a469983022f5078cf4bbb.png
[4]: http://5b0988e595225.cdn.sohucs.com/images/20171028/1b9a0bc769184d02b5e29822b56bc8ea.jpeg
[5]: http://5b0988e595225.cdn.sohucs.com/images/20171028/947a5391ed5e417587395e1d08104a10.jpeg
[6]: http://5b0988e595225.cdn.sohucs.com/images/20171028/cc49dbed99cf40238ba6f5b66dcdfeb4.jpeg

---

# Network Report

## 定义

计算机网络（英语：computer network）是指利用通信设备和线路将地理位置不同的、功能独立的多个计算机系统连接起来，以功能完善的网络软件实现网络的硬件、软件及资源共享和信息传递的系统。

简单的说即连接两台或多台计算机进行通信的系统。

计算机网络具有多种不同的拓扑结构，主要有星状、总线状、分布式、树状、网状、环状等。

## 分类

计算机网络可以按网络规模分为局域网、城域网、广域网、互联网。

### 局域网(Local Area Network, LAN)

![此处输入图片的描述][7]

局域网指处于同一建筑物或方圆数千米内的专用网络。局域网常用于连接公司办公室或大学里的计算机。

局域网具有如下特征：
* 覆盖范围较小，单个网络内包含用户少，设计、管理相对简单
* 传输速度快，延迟低，出错率低

### 城域网(Metropolitan Area Network, MAN)

![此处输入图片的描述][8]

城域网与局域网技术相似，可以看作是局域网的扩展。城域网常用于一个城市不同地域内的计算机互联，一个城域网中往往连接着多个局域网。

城域网具有如下特征：
* 覆盖范围与传输速度介于局域网和广域网之间
* 多用于连接局域网

### 广域网(Wide Area Network, WAN)

![此处输入图片的描述][9]

广域网可以覆盖几百几千公里的地域，能够包括一个国家甚至一片大陆，用于不同的LAN或MAN的互联。

广域网具有如下特征：
* 覆盖范围大，包含用户多
* 因为距离较远，信息衰减比较严重，所以一般要租用专线
* 因为所连接的用户多，总出口带宽有限，所以用户的终端连接速率一般较低

### 互联网(internet)

![此处输入图片的描述][10]

互联网指通过交换机以一组协议连接的不同的网络的集合。常见的互联网是通过WAN连接的LAN的集合。

## 性能指标

### 速率

速率指连接在计算机网络上的主机在数字信道上传送数据的速率，它也称为数据率（data rate）或比特率（bit rate）。速率是计算机网络中最重要的一个性能指标。速率的单位是bit/s（比特每秒，即bit per second）。

### 带宽

带宽表示在单位时间内从网络中的某一点到另一点所能通过的“最高数据率”。带宽的单位是“比特每秒”，记为bit/s。

### 吞吐量

吞吐量表示在单位时间内通过某个网络（或信道、接口）的数据量。吞吐量受网络的带宽或网络的额定速率的限制。例如，对于一个100Mbit/s的以太网，其额定速率是100Mbit/s，那么这个数值也是该以太网的吞吐量的绝对上限值。因此，对100Mbit/s的以太网，其典型的吞吐量可能也只有70Mbit/s。有时吞吐量还可用每秒传送的字节数或帧数来表示。

### 时延
时延是指数据（一个报文或分组，甚至比特）从网络（或链路）的一端传送到另一端所需的时间。时延是个很重要的性能指标，它有时也称为延迟或迟延。网络中的时延是由以下几个不同的部分组成的。

* 发送时延。
发送时延是主机或路由器发送数据帧所需要的时间，也就是从发送数据帧的第一个比特算起，到该帧的最后一个比特发送完毕所需的时间。因此发送时延也叫做传输时延。发送时延的计算公式是：
发送时延=数据帧长度（bit/s）/信道带宽（bit/s）
由此可见，对于一定的网络，发送时延并非固定不变，而是与发送的帧长（单位是比特）成正比，与信道带宽成反比。

* 传播时延。
传播时延是电磁波在信道中传播一定的距离需要花费的时间。传播时延的计算公式是：
传播时延=信道长度（m）/电磁波在信道上的传播速率（m/s）
电磁波在自由空间的传播速率是光速，即3.0×10km/s。电磁波在网络传输媒体中的传播速率比在自由空间要略低一些。

* 处理时延。
主机或路由器在收到分组时要花费一定的时间进行处理，例如分析分组的首部，从分组中提取数据部分，进行差错检验或查找适当的路由等，这就产生了处理时延。

* 排队时延。
分组在经过网络传输时，要经过许多的路由器。但分组在进入路由器后要先在输入队列中排队等待处理。在路由器确定了转发接口后，还要在输出队列中排队等待转发。这就产生了排队时延。

这样，数据在网络中经历的总时延就是以上四种时延之和：
总时延=发送时延+传播时延+处理时延+排队时延

* 时延带宽积。
把以上讨论的网络性能的两个度量—传播时延和带宽相乘，就得到另一个很有用的度量：传播时延带宽积，即时延带宽积=传播时延×带宽。

* 往返时间（RTT）。
在计算机网络中，往返时间也是一个重要的性能指标，它表示从发送方发送数据开始，到发送方收到来自接收方的确认（接受方收到数据后便立即发送确认）总共经历的时间。

* 利用率。
利用率有信道利用率和网络利用率两种。信道利用率指某信道有百分之几的时间是被利用的（有数据通过），完全空闲的信道的利用率是零。网络利用率是全网络的信道利用率的加权平均值。

## 硬件设备

* 网络接口控制器（network interface controller，NIC），又称网络接口控制器，网络适配器（network adapter），网卡（network interface card），或局域网接收器（LAN adapter），是一块被设计用来允许计算机在计算机网络上进行通讯的计算机硬件。每一块网卡都有一个被称为MAC地址的独一无二的48位串行号，它被写在卡上的一块ROM中。在网络上的每一个计算机都必须拥有一个独一无二的MAC地址。没有任何两块被生产出来的网卡拥有同样的地址。

* 中继器（repeater）是一个将输入信号增强放大的模拟设备，用来加强缆在线的信号，把信号送得更远，以延展网上长度。当电子信号在电缆上传送时，由于信号在网络传输介质中有衰减和噪声，使有用的数据信号变得越来越弱，为了保证有用数据的完整性，并在一定范围内传送，要用中继器把接收到的弱信号放大以保持与原数据相同。

* 集线器（Ethernet hub）是指将多条以太网双绞线或光纤集合连接在同一段物理介质下的设备，它可以把信号分散到多条线上，让其链接的设备工作在同一网段。集线器上有多个I/O端口，信号从任意一个端口进入后，会从其他端口出现。集线器的一端有一个接口连接服务器，另一端有几个接口与网络工作站相连。集线器接口的多少决定网络中所连计算机的数目，常见的集线器接口有8个、12个、16个、32个等几种。

* 网关（Gateway）是连接两个不同网络协议、不同体系结构的计算机网络的设备。网关有两种：一种是面向连接的网关，一种是无连接的网关。

* 桥接器（network bridge），又称网桥，一种网上设备，负责网上桥接（network bridging）之用，它能将一个较大的局域网分割成多个网段，或者将两个以上的局域网（可以是不同类型的局域网）互连为一个逻辑局域网。网桥的功能就是延长网络跨度，同时提供智能化连接服务，即根据数据包终点地址处于哪一个网段来进行转发和滤除。

* 路由器（Router）是连接局域网与广域网的连接设备，在网络中起着数据转发和信息资源进出的枢纽作用，是网络的核心设备。路由器提供路由与转送两种重要机制：决定数据包从来源端到目的端所经过的路由路径（host到host之间的传输路径），这个过程称为路由；将路由器输入端的数据包移送至适当的路由器输出端（在路由器内部进行），这称为转送。当数据从某个子网传输到另一个子网时，要通过路由器来完成。路由器根据传输费用、转接时延、网络拥塞或信源和终点间的距离来选择最佳路径。

* 交换器（switch）是一种可以根据要传输的网络信息构造自己的“转发表”，做出转发决策的设备。它可以为接入交换机的任意两个网络节点提供独享的电信号通路。

* 调制解调器（modem）是一种能够使电脑通过电话线同其他电脑进行通信的设备。因为电脑采用数字信号处理数据，而电话系统则采用模拟信号传输数据。为了能利用电话系统来进行数据通信，必须实现数字信号与模拟式的互换。

* 服务器（server）通常是指那些具有较高计算能力，能够提供给多个用户使用的计算机。服务器是通过网络给客户端用户使用的，需要连续的工作在7X24小时环境。

* 防火墙（firewall）是位于两个(或多个)网上间，实行网上间访问或控制的一组组件集合之硬件或软件。

## 评价

在多种多样的网络中，使用最为广泛的当属以太网（ethernet）和无线局域网（WLAN）。相较之下，无线局域网更为方便自由，而以太网等有限局域网更为快速稳定。

一般的个人或家庭用户通常只需要路由器就能实现足够使用的网络连接，而学校、企业等大型单位则需要一套完整的硬件设备与高带宽的网络。选择设备与网络种类时应量力而行，按需分析。

## 参考资料

wikipedia, baidubaike

[7]:http://uploads.xuexila.com/allimg/1604/766-1604200U331217.jpg
[8]:https://i2.wp.com/www.apposite-tech.com/blog/wp-content/uploads/2017/09/LAN-MAN-WAN.jpg
[9]:http://www.brainbell.com/tutorials/Networking/images/01fig02.gif
[10]:http://www.iyunying.org/wp-content/uploads/2015/12/a3fed0c9d90cdeb9a1bac41f828885e6.jpg

# Storage(Ceph)

![Logo](http://docs.ceph.com/docs/master/_static/logo.png)

使用Ceph系统可以提供对象存储、块设备存储和文件系统服务，

基于Ceph的key-value存储和NoSQL存储也在开发中，让Ceph成为目前最流行的统一存储系统。

Ceph底层提供了分布式的RADOS存储，用与支撑上层的librados和RGW、RBD、CephFS等服务。Ceph实现了非常底层的object storage，是纯粹的SDS，并且支持通用的ZFS、BtrFS和Ext4文件系统，能轻易得Scale，没有单点故障。

把一份数据存储到一群server里：先计算Placement Group再计算OSD(Object Storage Device)



## Feature

1. 保存一个对象的过程——先构建了一个**逻辑层**，也就是池(pool)，用于保存对象。再将一个pool划分为若干的PG(归置组 Placement Group)。对对象名进行HASH后，存入PG。实际上，存在着多个pool，PG的实际编号就由`pool_id+.+PG_id`组成。**物理层**由若干的OSD组成，用CRUSH做映射。

1. CRUSH: Controlled Replication Under Scalable Hashing。计算PG->OSD的映射关系

   - 给出一个PG_ID，作为CRUSH_HASH的输入。
   - CRUSH_HASH(PG_ID, OSD_ID, r) 得出一个随机数(重点是随机数，不是HASH)。
   - 对于所有的OSD用他们的权重乘以每个OSD_ID对应的随机数，得到乘积。
   - 选出乘积最大的OSD。
   - 这个PG就会保存到这个OSD上。

   ![crush_algo](/Users/darlenelee/Documents/sjtu18/SE419/419_notes/Image/crush_algo.png)

2. RADOS

   Ceph的底层，本身也是分布式存储系统，CEPH所有的存储功能都是基于RADOS实现。

   RADOS采用C++开发，所提供的原生Librados API包括C和C++两种。Ceph的上层应用调用本机上的librados API，再由后者通过socket与RADOS集群中的其他节点通信并完成各种操作。

   ![rados](/Users/darlenelee/Documents/sjtu18/SE419/419_notes/Image/rados.png)

3. CephFS

   POSIX 兼容的文件系统，使用 Ceph 存储集群来存储数据。 

   Ceph 文件系统与 Ceph 块设备、同时提供 S3 和 Swift API 的 Ceph 对象存储、或者原生库（ librados ）一样，都使用着相同的 Ceph 存储集群系统。

   当前， CephFS 还缺乏健壮得像 ‘fsck’ 这样的检查和修复功能。存储重要数据时需小心使用，因为灾难恢复工具还没开发完。

   ![img](http://docs.ceph.org.cn/_images/ditaa-b5a320fc160057a1a7da010b4215489fa66de242.png)

## Pro

1. 开源系统，免费，初始成本低；
2. 统一存储架构(Block/File/Object)，存储特性丰富；
3. 设计理念先进，CRUSH算法和元数据动态子树分区；
4. 扩展性、安全性好，多个服务器保存副本；
5. 不存在单点故障和瓶颈；

## Con

1. 后期运维成本高；
2. 系统成熟度不够，生产环境具有一定的风险；

## Key indicator

测试方法：

> 找到 osd 的挂载盘  `lsblk -f`
>
> 测试集群内各节点间的网络IO `nc -v -l -n 17480 > /dev/null`
>
> 测试rados集群的性能
>
> 查看该池占用的资源 `rados -p benchmark df`
>
> 测试写性能 `rados bench -p benchmark 60  write`
>
> 测试读性能 `rados bench -p benchmark 60 [ seq | rand ]`

## Comment

​	Ceph由Sage Weil设计与发布，是一个分布式的、可扩展的、可靠性好的存储系统平台。其论文《CEPH: RELIABLE, SCALABLE, AND HIGH-PERFORMANCE DISTRIBUTED STORAGE》内容翔实，又被整理为三篇规模较小的论文分述三个部分，读来让人甚是头疼，因此借鉴了许多现有博客文章。Ceph整合对象存储，块存储和文件系统在一个系统中。通过逻辑层和物理层，使用CRUSH这个伪随机分布算法实现抽签安排功能，任何组件都可以独立找到每个对象的位置；只需要很少的metadata（cluster map）。Ceph相比其他分布式文件系统，设计理念更先进，但不够成熟、投入工业应用仍有风险。

Reference: 

http://docs.ceph.com/docs/master/#

https://ivanzz1001.github.io/records/post/ceph/2017/07/28/ceph-benchmark

https://ceph.com/ceph-storage/

https://tobegit3hub1.gitbooks.io/ceph_from_scratch/

https://www.zhihu.com/question/21718731

http://www.oschina.net/translate/crush-controlled-scalable-decentralized-placement-of-replicated-data?cmp&p=2#

https://www.cnblogs.com/chenxianpao/p/5568207.html


---

# CPU

## Introduction

A **central processing unit (CPU)** is the electronic circuitry within a computer that carries out the instructions of a computer program by performing the basic arithmetic, logical, control and input/output (I/O) operations specified by the instructions. The computer industry has used the term "central processing unit" at least since the early 1960s. Traditionally, the term "CPU" refers to a processor, more specifically to its processing unit and control unit (CU), distinguishing these core elements of a computer from external components such as main memory and I/O circuitry.  

This report mainly includes Intel x86 and hardware virtualization.

## Moore's law

Moore's law is the observation that the number of transistors in a dense integrated circuit doubles about every two years. The observation is named after Gordon Moore, the co-founder of Fairchild Semiconductor and Intel, whose 1965 paper described a doubling every year in the number of components per integrated circuit, and projected this rate of growth would continue for at least another decade. In 1975, looking forward to the next decade, he revised the forecast to doubling every two years. The period is often quoted as 18 months because of a prediction by Intel executive David House (being a combination of the effect of more transistors and the transistors being faster).

## Intel

Intel Corporation (commonly known as Intel and stylized as intel) is an American multinational corporation and technology company headquartered in Santa Clara, California, in the Silicon Valley and on 6 Campus Drive, Parsippany-Troy Hills, New Jersey. It is the world's second largest and second highest valued semiconductor chip maker based on revenue after being overtaken by Samsung, and is the inventor of the x86 series of microprocessors, the processors found in most personal computers (PCs). Intel supplies processors for computer system manufacturers such as Apple, Lenovo, HP, and Dell. Intel also manufactures motherboard chipsets, network interface controllers and integrated circuits, flash memory, graphics chips, embedded processors and other devices related to communications and computing.

## x86

### Overview

x86 is a family of backward-compatible instruction set architectures based on the Intel 8086 CPU and its Intel 8088 variant. The 8086 was introduced in 1978 as a fully 16-bit extension of Intel's 8-bit-based 8080 microprocessor, with memory segmentation as a solution for addressing more memory than can be covered by a plain 16-bit address. The term "x86" came into being because the names of several successors to Intel's 8086 processor end in "86", including the 80186, 80286, 80386 and 80486 processors.

![图片加载失败](https://upload.wikimedia.org/wikipedia/commons/2/23/Core_2_Duo_E6300.jpg)

### Architecture

The x86 architecture is a variable instruction length, primarily "CISC" design with emphasis on backward compatibility. The instruction set is not typical CISC, however, but basically an extended version of the simple eight-bit 8008 and 8080 architectures. Byte-addressing is enabled and words are stored in memory with little-endian byte order. Memory access to unaligned addresses is allowed for all valid word sizes. The largest native size for integer arithmetic and memory addresses (or offsets) is 16, 32 or 64 bits depending on architecture generation (newer processors include direct support for smaller integers as well). Multiple scalar values can be handled simultaneously via the SIMD unit present in later generations, as described below. Immediate addressing offsets and immediate data may be expressed as 8-bit quantities for the frequently occurring cases or contexts where a -128..127 range is enough. Typical instructions are therefore 2 or 3 bytes in length (although some are much longer, and some are single-byte).

To further conserve encoding space, most registers are expressed in opcodes using three or four bits, the latter via an opcode prefix in 64-bit mode, while at most one operand to an instruction can be a memory location. However, this memory operand may also be the destination (or a combined source and destination), while the other operand, the source, can be either register or immediate. Among other factors, this contributes to a code size that rivals eight-bit machines and enables efficient use of instruction cache memory. The relatively small number of general registers (also inherited from its 8-bit ancestors) has made register-relative addressing (using small immediate offsets) an important method of accessing operands, especially on the stack. Much work has therefore been invested in making such accesses as fast as register accesses, i.e. a one cycle instruction throughput, in most circumstances where the accessed data is available in the top-level cache.

## Hardware Virtualization

### Intel virtualization (VT-x)

Previously codenamed "Vanderpool", VT-x represents Intel's technology for virtualization on the x86 platform. On November 13, 2005, Intel released two models of Pentium 4 (Model 662 and 672) as the first Intel processors to support VT-x. The CPU flag for VT-x capability is "vmx"; in Linux, this can be checked via /proc/cpuinfo, or in macOS via sysctl machdep.cpu.features.

"vmx" stands for Virtual Machine Extensions, which adds ten new instructions: VMPTRLD, VMPTRST, VMCLEAR, VMREAD, VMWRITE, VMCALL, VMLAUNCH, VMRESUME, VMXOFF, and VMXON. These instructions permit entering and exiting a virtual execution mode where the guest OS perceives itself as running with full privilege (ring 0), but the host OS remains protected.

As of 2015, almost all newer server, desktop and mobile Intel processors support VT-x, with some of the Intel Atom processors as the primary exception. With some motherboards, users must enable Intel's VT-x feature in the BIOS setup before applications can make use of it.

Intel started to include Extended Page Tables (EPT), a technology for page-table virtualization, since the Nehalem architecture, released in 2008. In 2010, Westmere added support for launching the logical processor directly in real mode – a feature called "unrestricted guest", which requires EPT to work.

Since the Haswell microarchitecture (announced in 2013), Intel started to include VMCS shadowing as a technology that accelerates nested virtualization of VMMs. The virtual machine control structure (VMCS) is a data structure in memory that exists exactly once per VM, while it is managed by the VMM. With every change of the execution context between different VMs, the VMCS is restored for the current VM, defining the state of the VM's virtual processor. As soon as more than one VMM or nested VMMs are used, a problem appears in a way similar to what required shadow page table management to be invented, as described above. In such cases, VMCS needs to be shadowed multiple times (in case of nesting) and partially implemented in software in case there is no hardware support by the processor. To make shadow VMCS handling more efficient, Intel implemented hardware support for VMCS shadowing.

## Comment

- Nowadays Moore's Law is expired and CPU's development become smooth. The important problem is how to make the best use of existing resources.
- Hence, I think Hardware Virtualization is one of the ways to gather and alloc resources.
