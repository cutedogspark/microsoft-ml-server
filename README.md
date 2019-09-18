# Welcome to ML-Server 👋
![Version](https://img.shields.io/badge/version-v0.0.1-blue.svg?cacheSeconds=2592000)
[![Twitter: cutedogspark](https://img.shields.io/twitter/follow/cutedogspark.svg?style=social)](https://twitter.com/cutedogspark)

## Build

```
docker-compose build
```

## Run

```
docker-compose up -d
```

## Scale

```
docker-compose scale computenode=3 webnode=3
```

## Exec Sql command 

```
/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P "{password}"
```

## Enable T-sql script (sql)

```sql
sp_configure 'external scripts enabled'
EXEC sp_configure 'external scripts enabled', 1
RECONFIGURE WITH OVERRIDE
GO
sp_configure 'external scripts enabled'
GO
```

## Python Sample

```
EXECUTE sp_execute_external_script
@language =N'Python',
@script=N'import sys
print(sys.version)';
GO
```

## R Sample

```
EXEC sp_execute_external_script   
@language =N'R', 
@script=N' 
OutputDataSet <- InputDataSet', 
@input_data_1 =N'SELECT 1 AS hello' 
WITH RESULT SETS (([hello] int not null)); 
GO 
```

## Run Ml-Server

```
az mlserver admin node setup --computenode
az mlserver admin node setup --webnode --admin-password Test1234@ --confirm-password Test1234@  --uri http://localhost:12805
az mlserver admin node stop --webnode
vim /opt/microsoft/mlserver/9.4.7/o16n/Microsoft.MLServer.WebNode/appsettings.json

ConnectionStrings->sqlserver->Connection => "Server=sql-server,1433;Initial Catalog=mlserver; Integrated Security=False; User Id=SA;Password=aWR>GxQgk6bNe2D;"
ConnectionStrings->sqlserver->Enable => true

az mlserver admin node start --webnode
```

jupyter 

```
/opt/microsoft/mlserver/9.4.7/runtime/python/bin/jupyter notebook list
```

## Author

👤 **Ming-Jui Chen**

* Twitter: [@cutedogspark](https://twitter.com/cutedogspark)
* Github: [@cutedogspark](https://github.com/cutedogspark)

## Show your support

Give a ⭐️ if this project helped you!


***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_


