==================
rqalpha-mod-sentry
==================


RQAlpha 集成 `Sentry`_ 日志收集 Mod

Sentry 是一个开源的实时错误收集平台，您可以通过 Sentry 快速查看和追踪错误日志。

您可以选择使用 `Sentry 线上平台`_ ，也可以选择自己搭建 `Sentry Server`_

当您已经获取 Sentry Server Url (类似于 'https://<key>:<secret>@sentry.io/<project>' )，就可以通过该 Mod 将 RQAlpha 运行的日志集成至 Sentry 了。

安装前
====================================

请务必确认已经参考 `RQAlpha 安装指南`_ 安装了最新版本的 RQAlpha

安装 rqalpha-mod-sentry
====================================

当 RQAlpha 安装之后，你可以执行以下命令来安装/卸载该 Mod:

..  code-block::

    # 安装
    $ rqalpha mod install sentry

    # 卸载
    $ rqalpha mod uninstall sentry

之后您可以执行以下命令来启动/关闭该 Mod:

..  code-block::

    # 启用
    $ rqalpha mod enable sentry

    # 关闭
    $ rqalpha mod disable sentry

配置项
====================================

*   url: <str> 需要指定 sentry 系统所对应的路径，比如 https://****@sentry.io/rqalpha_sample'
*   tags: <list> 指定您希望发送日志时包含的 config 参数。因为参数是多级的，我们约定以 `__` 来区分，比如说想指定 :code:`mod.sys_risk.validate_position` 在 sentry 日志中显示，则将其转换成 :code:`mod__sys_risk__validate_position`

如下是默认配置项:

..  code-block::

    {
        "url": None,
        "tags": [
            "base__start_date",
            "base__end_date",
            "base__stock_starting_cash",
            "base__future_starting_cash",
            "base__securities",
            "base__run_type",
            "base__frequency",
            "base__benchmark",
        ]
    }

您可以在您的 `config.yml` 文件中添加来修改默认配置

..  code-block::

    mod:
        url: https://your_own_domain@sentry.io/rqalpha_sample
        tags: [
            base__start_date
            base__end_date
            base__stock_starting_cash
            base__future_starting_cash
            base__securities
            base__run_type
            base__frequency
            base__benchmark
            mod__sys_risk__validate_position
        ]

您也可以直接在代码中指定配置信息:

..  code-block::

    from rqalpha import run
    config = {
        "base": {
            "strategy_file": "strategy.py",
            "securities": ["stock"],
            "start_date": "2015-01-09",
            "end_date": "2015-03-09",
            "frequency": "1d",
            "stock_starting_cash": 100000,
        }
        "mod": {
            "sentry": {
                "enabled": True,
                "url": "https://your_own_domain@sentry.io/rqalpha_sample",
                "tags": [
                    "base__start_date",
                    "base__end_date",
                    "base__stock_starting_cash",
                    "base__future_starting_cash",
                    "base__securities",
                    "base__run_type",
                    "base__frequency",
                    "base__benchmark",
                    "mod__sys_risk__validate_position"
                ]
            }
        }
    }
    run(config)

在启动该 Mod 的情况下，

您也可以直接通过 :code:`rqalpha run` 增加 `--sentry target_sentry_server_url` 选项来开启 Sentry 日志收集服务

.. code-block::

    $ rqalpha run -f strategy.py --sentry https://your_own_domain@sentry.io/rqalpha_sample

.. _Sentry: https://sentry.io/welcome/
.. _Sentry Server: https://docs.sentry.io/server/
.. _Sentry 线上平台: https://sentry.io/welcome/
.. _RQAlpha 安装指南: http://rqalpha.readthedocs.io/zh_CN/latest/intro/install.html

