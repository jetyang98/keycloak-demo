# keycloak-demo

> 本项目来源于 https://juejin.cn/post/6844903973741150215。

第一次安装 keycloak 使用命令 `docker run -d -p 8080:8080 -e KEYCLOAK_USER=admin -e KEYCLOAK_PASSWORD=admin --name keycloak quay.io/keycloak/keycloak:15.0.2`。

之后启动 keycloak 用命令 `docker start keycloak`。

**注意：**每次启动 keycloak 时会比较慢。

## vue-demo

前端项目。

**功能：**登录，获取 token。

## spring-boot-demo

后端项目。

**功能：**根据 token 验证权限。

## django_demo

后端项目，自己实现验证 token 的函数。
