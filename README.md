# Exec_aws_cli_Python

Pythonでaws cliコマンドを実行する。  
AWS Lambdaでbranch間のマージ可否を取得しようとしたが、awsコマンドが実行できないため、諦めた。記念に保存。

## 前提

1. aws-cliが実行できること。
2. 比較したいAWS CodeCommitリポジトリにaws-cliでアクセスできること。

## 実行

``` sh
python3 app.py
```

## 参考

- [Exec_Unix_Command_Python](https://github.com/SampleUser0001/Exec_Unix_Command_Python)
  - なんか同じようなことを過去にやってる