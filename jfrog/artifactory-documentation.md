# JFrog Artifactory Installation and Setup on Ubuntu!


## Step 1: Update the System
sudo apt update

## Step 2: Install Java
sudo apt install openjdk-8-jdk -y

## Step 3: Validate Java installation:
java -version
<img width="1081" height="98" alt="Screenshot from 2026-02-12 14-59-54" src="https://github.com/user-attachments/assets/418930ec-2685-4c35-9811-ca9d11e0847b" />

## Step 3: Download JFrog Artifactory
wget https://jfrog.bintray.com/artifactory/jfrog-artifactory-oss-6.9.6.zip

## Step 4: Install unzip (if not already installed)
sudo apt install unzip -y

## Step 5: Unzip Artifactory Package
unzip -o jfrog-artifactory-oss-6.9.6.zip -d /opt/

## Step 6: Navigate to Artifactory Directory
cd /opt/artifactory-oss-6.9.6

## Step 7: Start JFrog Artifactory
./bin/artifactory.sh start

## Step 8: Access Artifactory UI
Open your browser and go to: https://<your-server-ip>:8081
<img width="1848" height="833" alt="image" src="https://github.com/user-attachments/assets/635836d5-921c-4828-a75d-87076c99e7de" />

## Step 9: Set Admin Password
Follow the UI prompt to set the administrator password.

## Step 10: Select Package Types
Maven
Generic

## Step 11: Finish Setup

Click Finish to navigate to the home dashboard.
<img width="1848" height="833" alt="Screenshot from 2026-02-12 11-44-34" src="https://github.com/user-attachments/assets/65494a4b-c351-4ce0-a8df-203861236f67" />


## Step 12: Create a Generic Local Repository

### 12.1 Open Repository Configuration
Navigate: Admin → Repositories → Local → New Local Repository

### 12.2 Configure Repository
Package Type: Generic
Repository Key: generic-local

### 12.3 Save & Finish
<img width="1848" height="833" alt="Screenshot from 2026-02-12 11-49-21" src="https://github.com/user-attachments/assets/8792149a-7554-4d60-a17f-b676aca36f9b" />


### 12.4 Verify Repository
Go to Artifacts → You should see generic-local
<img width="1848" height="833" alt="Screenshot from 2026-02-12 11-50-42" src="https://github.com/user-attachments/assets/90d5a486-88ac-4dcd-bad5-ba571d500078" />


## Step 13: Create a Maven Local Repository

### 13.1 Open Repository Configuration
Navigate: Admin → Repositories → Local → New

### 13.2 Select Package Type
Maven

### 13.3 Configure Maven Repository
Repository Key: maven-local
Maven Snapshot Version Behavior: Unique
Handle Releases: Tick
Handle Snapshots: Tick
<img width="1848" height="833" alt="Screenshot from 2026-02-12 11-52-10" src="https://github.com/user-attachments/assets/b26c9b9f-5b1c-46c3-86d4-e7624f7b1957" />


### 13.4 Save & Finish
<img width="1848" height="833" alt="Screenshot from 2026-02-12 11-52-18" src="https://github.com/user-attachments/assets/1aa5ba10-f31e-4ff1-b3ef-783ff3bd3493" />

### 13.5 Verify Repository
Go to Artifacts → You should see maven-local

## Step 14: Prepare Test Files for Generic Repository
mkdir artifactory-test
cd artifactory-test
echo "Hello Artifactory" > test1.txt
echo "Generic Repo Upload" > test2.txt

## Step 15: Upload Test Files via Web UI

### 15.1 Navigate to Artifacts
Click generic-local
Click Deploy
Select test1.txt and test2.txt
Click Deploy
<img width="1793" height="746" alt="Screenshot from 2026-02-12 12-00-37" src="https://github.com/user-attachments/assets/01d7d1ab-c3ff-45ef-8ac6-1e349f803b46" />



