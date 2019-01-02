# Report 4

## Requirement 1

### ci/cd平台

- 采用drone搭建ci/cd平台，该工具语法简洁，和travis、gitlab-runner类似，jenkins则过于重量级。
- 首先需要一台服务器运行drone服务，它以容器方式运行，官方也给出了docker-compose示例。
- drone和github搭配是通过github的Oauth application，注册一个新的Oauth app，然后将账号传给drone即可。

### 配置集成项目

- 登陆drone服务，设置hook，让它监听需要持续集成的项目。
- 项目地址：[前端](https://github.com/Veiasai/bookstore_front)，[后端](https://github.com/Veiasai/bookstore_back)。
- 在分支drone-0.8上，根目录下创建.drone.yml文件，按照drone语法配置集成方式，整个过程是以容器运行的，可以利用各大镜像仓库里的镜像去完成工作，比如前端项目通过node镜像编译，nginx镜像部署，后端java项目则用maven镜像编译打包，tomcat镜像部署。

## Requirement 2

### rke部署k8s集群

- 相对来讲，在ubuntu上使用rke要比centOS简单，使用腾讯云的ubuntu 16.04的服务器，没有任何错误，一次成功。
- 在部署配置文件中，开启ingress-addons，则会启动ingress-controller和default-backend，就有了ingress功能，只需要写路由规则即可使用。
- Dashboard下载官方的yaml配置文件，修改镜像为`registry.cn-shenzhen.aliyuncs.com/rancher_cn/kubernetes-dashboard-amd64:v1.8`，则可以正常下载了。
- 访问dashboard则通过不设拦截的proxy，并未配置完善的权限管理。

## Requirement 3

### k8s部署前后端

- drone会将前后端都打包为镜像，并发布到docker hub，在k8s使用只需要写好部署文件即可，见k8s/bookstore目录，数据库则在k8s/mongo和k8s/mysql。

## Requirement 4

### Load Balace

- 在k8s上做LB并不复杂，实际上k8s暴露外部服务的方式只有三种，nodeport，ingress，外部负载均衡器。
- 前端的访问我们直接采用了nodeport，这个其实性能不高，资源损耗很大，但是比较简单，直接从各个ip都可以访问到前端。
- 后端的访问使用ingress-controller，这个可以通过域名转发http请求，详细的见配置文件k8s/bookstore/bookstore-ingress.yml。

### Experiment

----------
## 实验背景 ##

 - 测试工具：Jmeter 
 - 请求规模：设置了100个线程，启动时间1s，10~20次循环，对后端中最常用的查询功能进行了测试。
 - replica数量：限于集群规模，测试了1~4台replica情况下的表现。

----------
## 测试结果 ##

replica=1，循环次数=10
![config](Image/experiment/1-1.png)

replica=2，循环次数=20
![config](Image/experiment/2.jpg)

replica=3，循环次数=20
![config](Image/experiment/3.jpg)

replica=4，循环次数=20
![config](Image/experiment/4.jpg)


----------


## 测试分析 ##
#### Throughput（RPS） ####

![config](Image/experiment/chart1.png)

由测试数据可见，在replica数量从1增加为2时RPS的提升极其明显，但直到其数目提升到4，RPS并未出现可见的提升，相反还出现了细微的下降，这可能是由于两台replica已经足以处理测试的请求，而且分发到不同的replica的过程又需要一些时间所导致的。（之所以未继续增大测试规模是由于网速限制故继续增加测试规模已无太大意义）

#### Response Time ####

![config](Image/experiment/chart2.png)

由测试数据可见，Average Response Time也随replica数量增多而出现先迅速下降后缓慢上升的情况，与RPS测试结果相符，但是值得留意的是，replica=3的情况下90%line、95%line、99%line的时间均比replica=2要稍小一些，replica=4也有类似的现象，不确定这是由于测试的随机性导致的还是replica增加时对其有相对更明显的效果。

## Requirement 5

### Monitor

- 为了监测集群资源使用，我们安装了grafana和prometheus去监控集群资源使用，这部分的配置文件直接使用官方教程给出的。

#### master/node节点环境部署

以下使用的配置文件均位于文件夹k8s-prometheus-grafana中。  
在master节点按照配置文件进行安装部署，并在node节点通过以下操作下载监控所需镜像。

`docker pull prom/node-exporter`  
`docker pull prom/prometheus:v2.0.0`  
`docker pull grafana/grafana:4.2.0`  

采用daemonset方式部署node-exporter组件

`kubectl create -f  node-exporter.yaml` 

#### 部署prometheus组件

* rbac文件

    `kubectl create -f  k8s-prometheus-grafana/prometheus/rbac-setup.yaml`

* 以configmap的形式管理prometheus组件的配置文件

    `kubectl create -f  k8s-prometheus-grafana/prometheus/configmap.yaml`

* Prometheus deployment 文件

    `kubectl create -f  k8s-prometheus-grafana/prometheus/prometheus.deploy.yml`

* Prometheus service文件

    `kubectl create -f  k8s-prometheus-grafana/prometheus/prometheus.svc.yml`

#### 部署grafana组件

* grafana deployment配置文件

    `kubectl create -f   k8s-prometheus-grafana/grafana/grafana-deploy.yaml`

* grafana service配置文件

    `kubectl create -f   k8s-prometheus-grafana/grafana/grafana-svc.yaml`

* grafana ingress配置文件

    `kubectl create -f   k8s-prometheus-grafana/grafana/grafana-ing.yaml`

##### 配置效果

![config](Image/prometheus.png)

##### 运行效果

![config](Image/grafana.png)

### Autoscaling

- 运行metrics-server服务，将replica controller替换为deployment，设置cpu资源limit，最后创建hpa资源。
- 程序启动时由于占用了较高cpu资源，会发生一次scale，稳定后将会降回1个pod，然后发起测试请求，观察grafana性能监控曲线。

![grafana](Image/autoscaling.png)

- 由上图，可以看见。
  - 在3:30开始运行测试，单个pod的cpu使用率开始上升，当达到limit 0.5core时，开始scale。
  - 经过30s，另外三个pod开始调度运行。
  - 三个pod的tomcat应用开始启动，tomcat加载也较慢。
  - 经过30s，tomcat启动完毕。
  - mysql的资源使用率随着pod增加不断上升。
  - 当四个pod同时工作，单个的资源使用率开始下降并趋于稳定(0.25)。

- Autoscaling总耗时约一分钟。
  - 调度反应很快，大约几秒。
  - 容器启动时间在二十秒左右。
  - tomcat启动需要三十秒。

## 参考文件

https://github.com/redhatxl/k8s-prometheus-grafana.git
