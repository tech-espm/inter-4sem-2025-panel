-- Esse script vale para o MySQL 8.x. Se seu MySQL for 5.x, precisa executar essa linha comentada:
-- CREATE DATABASE IF NOT EXISTS sensores;
CREATE DATABASE IF NOT EXISTS panel DEFAULT CHARACTER SET utf8mb4 DEFAULT COLLATE utf8mb4_0900_ai_ci;

-- Todos os deltas estão em segundos

USE panel;

-- Sensores Steinel

-- Cada uma das 8 zonas (0 ... 7) será mapeada como um id_sensor (1 ... 8)
-- topic espm/stainel/hpd/DetectedPersonsZone
-- {"DetectedPersonsZone":[0,0,2,1,1,0,1,0]}
-- topic espm/stainel/hpd/LuxZone
-- {"LuxZone":[70.00,78.00,74.00,87.00,67.00,57.00,50.00,53.00]}
-- topic espm/stainel/hpd/Humidity
-- {"Humidity":67.00}
-- topic espm/stainel/hpd/Temperature
-- {"Temperature":24.30}
CREATE TABLE pca (
  id bigint NOT NULL,
  data datetime NOT NULL,
  id_sensor tinyint NOT NULL,
  delta int NOT NULL, -- O campo delta diz respeito a alterações no valor de pessoas
  pessoas tinyint NOT NULL,
  luminosidade float NOT NULL,
  umidade float NOT NULL,
  temperatura float NOT NULL,
  PRIMARY KEY (id),
  KEY pca_data_id_sensor (data, id_sensor),
  KEY pca_id_sensor (id_sensor)
);

-- Só existe id_sensor 1
-- topic espm/stainel/mtp/Brightness1
-- {"Brightness1": 51,"clientId":"mtp"}
-- topic espm/stainel/mtp/Humidity
-- {"Humidity": 65.10,"clientId":"mtp"}
-- topic espm/stainel/mtp/Temperature
-- {"Temperature": 22.41,"clientId":"mtp"}
-- topic espm/stainel/mtp/VOC
-- {"VOC": 102,"clientId":"mtp"}
-- topic espm/stainel/mtp/CO2
-- {"CO2": 465,"clientId":"mtp"}
-- topic espm/stainel/mtp/AirPressure
-- {"AirPressure": 934.50,"clientId":"mtp"}
-- topic espm/stainel/mtp/Noise
-- {"Noise": 44,"clientId":"mtp"}
-- topic espm/stainel/mtp/AerosolStaleAirStatus
-- {"AerosolStaleAirStatus": 1,"clientId":"mtp"}
-- topic espm/stainel/mtp/AerosolRiskOfInfectionStatus
-- {"AerosolRiskOfInfectionStatus": 1,"clientId":"mtp"}
-- topic espm/stainel/mtp/DewPoint
-- {"DewPoint": 15.39,"clientId":"mtp"}
CREATE TABLE creative (
  id bigint NOT NULL,
  data datetime NOT NULL,
  id_sensor tinyint NOT NULL,
  delta int NOT NULL,
  luminosidade float NOT NULL,
  umidade float NOT NULL,
  temperatura float NOT NULL,
  voc float NOT NULL,
  co2 float NOT NULL,
  pressao_ar float NOT NULL,
  ruido float NOT NULL,
  aerosol_parado tinyint NOT NULL,
  aerosol_risco tinyint NOT NULL,
  ponto_orvalho float NOT NULL,
  PRIMARY KEY (id),
  KEY creative_data_id_sensor (data, id_sensor),
  KEY creative_id_sensor (id_sensor)
);

-- Sensores Milesight

-- O timestamp foi removido do banco porque ele não seguia um padrão crescente quando recebido dos sensores

-- topic v3/espm/devices/soil01/up
-- topic v3/espm/devices/soil02/up
-- { "end_device_ids": { "device_id": "soil01" }, "uplink_message": { "rx_metadata": [{ "timestamp": 2040934975 }], "decoded_payload" : { "conductivity": 114, "humidity": 24.5, "temperature": 23.2 } } }
CREATE TABLE solo (
  id bigint NOT NULL,
  data datetime NOT NULL,
  id_sensor tinyint NOT NULL,
  delta int NOT NULL,
  condutividade float NOT NULL,
  umidade float NOT NULL,
  temperatura float NOT NULL,
  PRIMARY KEY (id),
  KEY solo_data_id_sensor (data, id_sensor),
  KEY solo_id_sensor (id_sensor)
);

-- topic v3/espm/devices/odor01/up
-- topic v3/espm/devices/odor02/up
-- { "end_device_ids": { "device_id": "odor01" }, "uplink_message": { "rx_metadata": [{ "timestamp": 2040934975 }], "decoded_payload": { "battery": 99, "h2s": 0.02, "humidity": 78, "nh3": 0.01, "temperature": 24.3 } } }
CREATE TABLE odor (
  id bigint NOT NULL,
  data datetime NOT NULL,
  id_sensor tinyint NOT NULL,
  delta int NOT NULL,
  bateria tinyint NOT NULL,
  h2s float NOT NULL,
  umidade float NOT NULL,
  nh3 float NOT NULL,
  temperatura float NOT NULL,
  PRIMARY KEY (id),
  KEY odor_data_id_sensor (data, id_sensor),
  KEY odor_id_sensor (id_sensor)
);

-- topic v3/espm/devices/presence01/up
-- topic v3/espm/devices/presence02/up
-- topic v3/espm/devices/presence03/up
-- topic v3/espm/devices/presence04/up
-- topic v3/espm/devices/presence05/up
-- topic v3/espm/devices/presence06/up
-- topic v3/espm/devices/presence07/up
-- topic v3/espm/devices/presence08/up
-- { "end_device_ids": { "device_id": "presence01" }, "uplink_message": { "rx_metadata": [{ "timestamp": 2040934975 }], "decoded_payload": { "battery": 99, "occupancy": "vacant" } } }
CREATE TABLE presenca (
  id bigint NOT NULL,
  data datetime NOT NULL,
  id_sensor tinyint NOT NULL,
  delta int NOT NULL,
  bateria tinyint NOT NULL,
  ocupado tinyint NOT NULL,
  PRIMARY KEY (id),
  KEY presenca_data_id_sensor (data, id_sensor),
  KEY presenca_id_sensor (id_sensor)
);


-- topic v3/espm/devices/temperature01/up
-- { "end_device_ids": { "device_id": "temperature01" }, "uplink_message": { "rx_metadata": [{ "timestamp": 2040934975 }], "decoded_payload": { "humidity": 82, "temperature": 23.4 } } }
CREATE TABLE temperatura (
  id bigint NOT NULL,
  data datetime NOT NULL,
  id_sensor tinyint NOT NULL,
  delta int NOT NULL,
  umidade float NOT NULL,
  temperatura float NOT NULL,
  PRIMARY KEY (id),
  KEY temperatura_data_id_sensor (data, id_sensor),
  KEY temperatura_id_sensor (id_sensor)
);

-- topic v3/espm/devices/passage01/up
-- topic v3/espm/devices/passage02/up
-- { "end_device_ids": { "device_id": "passage01" }, "uplink_message": { "rx_metadata": [{ "timestamp": 2040934975 }], "decoded_payload": { "battery": 0, "period_in": 0, "period_out": 0 } } }
CREATE TABLE passagem (
  id bigint NOT NULL,
  data datetime NOT NULL,
  id_sensor tinyint NOT NULL,
  delta int NOT NULL,
  bateria tinyint NOT NULL,
  entrada int NOT NULL,
  saida int NOT NULL,
  PRIMARY KEY (id),
  KEY passagem_data_id_sensor (data, id_sensor),
  KEY passagem_id_sensor (id_sensor)
);

-- Queries de consolidação

-- Query de consolidação de ocupação máxima por zona por dia do mês e por hora, para o heatmap de visão explodida por dia do mês com N colunas e 24 linhas
-- Para preencher os dias/horas faltantes:
-- Se o primeiro registro do dia não for às 00:00 preencher com 0 todas as horas das 00:00 até a primeira retornada
-- Os registros faltantes ao longo do dia devem ser preenchidos com o valor do campo ultimo_pessoas do último registro retornado
select tmp.id_sensor, tmp.dia, tmp.hora, tmp.pessoas, u.pessoas ultimo_pessoas from
(
	select id_sensor, date_format(date(data), '%d/%m/%Y') dia, extract(hour from data) hora, max(pessoas) pessoas, max(id) id_ultimo
	from pca
	where data between '2025-03-03 00:00:00' and '2025-03-14 23:59:59'
	group by id_sensor, dia, hora
	order by id_sensor, dia, hora
) tmp
inner join pca u on u.id = tmp.id_ultimo;

select date_format(date(data), '%d/%m/%Y') dia, extract(hour from data) hora, avg(luminosidade) luminosidade, avg(umidade) umidade, avg(voc) voc, avg(co2) co2, avg(pressao_ar) pressao_ar, avg(ruido) ruido, avg(ponto_orvalho) ponto_orvalho
from creative
where data between '2025-03-03 00:00:00' and '2025-03-14 23:59:59'
group by dia, hora
order by dia, hora;

select date_format(date(data), '%d/%m/%Y') dia, extract(hour from data) hora, avg(condutividade) condutividade, avg(umidade) umidade, avg(temperatura) temperatura
from solo
where data between '2025-03-03 00:00:00' and '2025-03-14 23:59:59'
group by dia, hora
order by dia, hora;

select date_format(date(data), '%d/%m/%Y') dia, extract(hour from data) hora, avg(bateria) bateria, avg(h2s) h2s, avg(umidade) umidade, avg(nh3) nh3, avg(temperatura) temperatura
from odor
where id_sensor = 1 and data between '2025-03-03 00:00:00' and '2025-03-14 23:59:59'
group by dia, hora
order by dia, hora;

select id_sensor, date(data) dia, avg(delta) presenca_media
from presenca
where data between '2025-03-10 00:00:00' and '2025-03-14 23:59:59' and ocupado = 0
group by id_sensor, dia
order by id_sensor, dia;

select date_format(date(data), '%d/%m/%Y') dia, extract(hour from data) hora, avg(umidade) umidade, avg(temperatura) temperatura
from temperatura
where id_sensor = 1 and data between '2025-03-03 00:00:00' and '2025-03-14 23:59:59'
group by dia, hora
order by dia, hora;

select date_format(date(data), '%d/%m/%Y') dia, extract(hour from data) hora, sum(entrada) entrada, sum(saida) saida
from passagem
where id_sensor = 2 and data between '2025-03-03 00:00:00' and '2025-03-14 23:59:59'
group by dia, hora;
