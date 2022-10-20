# Databricks notebook source
import mlflow

model = mlflow.sklearn.load_model("models:/dota-unesp/production")

sdf = spark.table("sandbox_apoiadores.abt_dota_pre_match_new")
df = sdf.toPandas()

# COMMAND ----------

features = list(set(df.columns.tolist())-set(["match_id","radian_win"]))

x = df[features]

# COMMAND ----------

score = model.predict_proba(x)

df["proba_randian_win"] = score[:,1]
df[["match_id","radian_win","proba_randian_win"]]
