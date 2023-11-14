# dot_config
我的配置,我使用了git bash作为了默认的终端，主要配置了
* git
* git-bast
* scoop 安装程序,查看 `doc/soft/scoop.py`


## 前置
* git 
* scoop
* make (可选)

## 使用

* 复制 `settings.yaml.demo` 到 `settings.yaml` 修改相应的配置
* 修改`settings.yaml`的配置
* 安装依赖
  ```
  make ensure
  # 没有make 
  pipenv sync --dev
  env clean
  ```
* 使用
  ```
  ### 安装 
  make install 
  # 没有make 
  python main.py install
  
  
  ### 卸载
  make uninstall 
  # 没有make 
  python main.py uninstall
  ```
* 最后需要手动source .bashrc


## 参考
* https://github.com/xnng/my-git-bash
* https://github.com/hongwenjun/tmux_for_windows
* https://github.com/ohmybash/oh-my-bash
* https://github.com/junegunn/fzf
* https://github.com/LKI/LKI


