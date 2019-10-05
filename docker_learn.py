# todo  1、docker pull jenkins  2、docker run -d --name myjenkins -p 8080:8080 jenkins

# todo  4、docker exec -it myjenkins bash:表示容器进行shell交互
# todo  5、 docker stats myjenkins ：查看容器运行时的性能信息
# todo  6、docker inspect myjenkins:返回容器的所有原信息
# todo  7、docker rm -f myjenkins:强制删除容器

# todo  8、docker logs -f myjenkins:查看容器的日志
# todo  9、docker cp `pwd`/jenkins.war  myjenkins:/  :将jenkins.war文件复制到容器myjenkins根目录下
# todo  10、docker commit myjenkins jialu:制作镜像
# todo  11、docker run --name some-mysql -v /home/yang/mysql:/var/lib/mysql
#            -e MYSQL_ROOT_PASSWORD=123456 -p 9999:3306 -d mysql

# todo  12、docker run --name chrome -e NODE_MAX_INSTANCES=6 -e NODE_MAX_SESSION=6
#           -e DBUS_SESSION_BUS_ADDRESS=/dev/null  --link hub -d  selenium/node-chrome-debug