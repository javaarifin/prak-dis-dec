# LAPORAN PRAKTIKUM SISTEM TERDISTRIBUSI DAN TERDESENTRALISASI #

---
## Minggu 4

------
Nama    : Muhammad Java Arifin

NIM     : 235410073

-----
## Konsistensi dan Replikasi pada Sistem Terdistribusi

### Streaming Replication Menggunakan PostgreSQL
Materi ini membahas tentang cara mengkonfigurasi streaming replication di PostgreSQL 18.
Secara prinsip, sebenarnya sama dengan versi-versi PostgreSQL sebelumnya, hanya saja
letak dari direktori data bukan di /var/lib/postgresql/data lagi tapi berubah di
/var/lib/postgresql/18/docker. Materi ini ditulis berdasarkan materi pada
https://medium.com/@eremeykin/how-to-setup-single-primary-postgresql-replication-with-do
cker-compose-98c48f233bbf dengan perubahan signifikan. Kerjakan materi pada bagian ini
dan buat penjelasannya di repo GitHub anda sesuai dengan ketentuan.

#### 1.  Prasyarat

    Install Docker
    ![](Images/Cek%20versi%20docker.png)

#### 2. Struktur Folder

        ![](Images/susunan%20folder.png)

            00_init.sql
            ![](Images/init%20sqll.png)

            docker-compose.yaml
            
            Isi file diatas

            x-postgres-common: &postgres-common
            image: postgres:18.3-alpine3.23
            user: postgres
            restart: always
            healthcheck:
                test: ["CMD-SHELL", "pg_isready -U zuser -d zdb"]
                interval: 10s
                timeout: 5s
                retries: 5

            services:
            postgres_primary:
                <<: *postgres-common
                ports:
                - "5432:5432"
                environment:
                POSTGRES_USER: zuser
                POSTGRES_DB: zdb
                POSTGRES_PASSWORD: zpass
                POSTGRES_HOST_AUTH_METHOD: "scram-sha-256\nhost replication replicator 0.0.0.0/0 md5"
                POSTGRES_INITDB_ARGS: "--auth-host=scram-sha-256"
                command: |
                postgres
                -c wal_level=replica
                -c hot_standby=on
                -c max_wal_senders=10
                -c max_replication_slots=10
                -c hot_standby_feedback=on
                volumes:
                - ./00_init.sql:/docker-entrypoint-initdb.d/00_init.sql

            postgres_replica:
                <<: *postgres-common
                ports:
                - "5433:5432"
                environment:
                PGUSER: replicator
                PGPASSWORD: replicator_password
                PGDATA: /var/lib/postgresql/18/docker
                command: |
                bash -c "
                until pg_basebackup --pgdata=/var/lib/postgresql/18/docker -R --slot=replication_slot --host=postgres_primary --port=5432 -X stream; do
                    echo 'pg_basebackup failed. Retrying in 5 seconds ...'
                    sleep 5
                done
                echo 'Backup done, starting replica...'
                chmod 0700 /var/lib/postgresql/18/docker
                postgres
                "
                depends_on:
                - postgres_primary

    env.sh
    
    code file diatas

        alias dcu="sudo docker-compose up -d"
        alias dcd="sudo docker-compose down"
        alias dps="sudo docker ps"
        alias der="sudo docker exec -it <nama-direktori>-postgres_replica-1 bash"
        alias dep="sudo docker exec -it <nama-direktori>-postgres_primary-1 bash"
        alias dlr="sudo docker logs <nama-direktori>-postgres_replica-1"
        alias dlp="sudo docker logs <nama-direktori>-postgres_primary-1"


#### 3. Menjalankan Docker-compose
![](Images/menjalankan%20.png)

Cek kedua image
![](Images/cek%20images.png)

#### 4. Pengujian 
![](Images/pengujian%201.png)
    

![](Images/pengujian%202.png)

Uji replika data

![](Images/uji%20replika.png)

![](Images/pg_promote.png)

![](Images/pg_recovery.png)

![](Images/docker%20down.png)


## Replikasi Master-Master Menggunakan Apache Ignite

#### 1. Buat folder baru 

![](Images/folderbaruignite.png)

#### 2. Buat isi file docker-compose


        name: ignite3

        x-ignite-def: &ignite-def
        image: apacheignite/ignite:3.1.0
        environment:
            JVM_MAX_MEM: "4g"
            JVM_MIN_MEM: "4g"
        configs:
            - source: node_config
            target: /opt/ignite/etc/ignite-config.conf

        services:
        node1:
            <<: *ignite-def
            command: --node-name node1
            ports:
            - "10300:10300"
            - "10800:10800"
        node2:
            <<: *ignite-def
            command: --node-name node2
            ports:
            - "10301:10300"
            - "10801:10800"
        node3:
            <<: *ignite-def
            command: --node-name node3
            ports:
            - "10302:10300"
            - "10802:10800"

        configs:
        node_config:
            content: |
            ignite {
                network {
                port: 3344
                nodeFinder.netClusterNodes = ["node1:3344", "node2:3344", "node3:3344"]
                }
            }
    
### 3. Jalankan node
![](Images/jlnkan%20node.png)

### 4. Jalankan CLI ignite
![](Images/CLI%20ignite.png)

![](Images/CLI%20lanjut.png)

### 5.  masukan folder sql

![](Images/folder%20sql.png)