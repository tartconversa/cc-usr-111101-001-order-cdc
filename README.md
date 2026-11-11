# 复合门店订单 CDC 的事务边界与断点恢复

本项目保存公园阅读空间经营数据格式与原始资料读取程序。当前读取器只输出输入类型和条数，不加工业务事实，不修改数据。资料中的标识、数量和金额均为合成值。

## 格式与目录

fixtures 保存输入，src/source_reader.py 为读取入口，tests 核对读取行为。offset 在每个 source 内从1递增；source_version 是全业务键版本。kind 为 BEGIN、CHANGE、COMMIT，entity 为 order 或 refund，op 为 UPSERT 或 DELETE。items 按品类保存金额分。事务变更不包括边界消息。

## 运行命令

Python 3.11 及以上，只使用标准库，无第三方安装步骤。进入项目根目录运行：

    python -m src.source_reader fixtures/transactions.jsonl

编译检查：

    python -m compileall -q src tests

读取测试：

    python -m unittest discover -s tests -v

## 容器方式

    docker build -t order-cdc:local .
    docker run --rm order-cdc:local

容器默认执行读取测试。数据加工输出请写入独立路径，避免覆盖原始资料。
