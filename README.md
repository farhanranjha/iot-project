# IOT Data Collection Project

This project consists of two main components: a Django REST API server for receiving IoT data and a MicroPython script running on ESP32 for sending sensor data.

## Project Structure

### Server (Django REST API)

The server is built using Django with Django REST Framework and is hosted at: **https://iot.internal.ripeseed.io**

### MicroPython ESP32 Script

The ESP32 script is located in the `script/` folder at the project root, specifically in `script/ping.py`.

---

## MicroPython ESP32 Script

The ESP32 script (`script/ping.py`) is divided into three main functions:

### 1. Wi-Fi Connection Function

- **Purpose**: Establishes connection to Wi-Fi network
- **Configuration**: Uses SSID and password for authentication
- **Timeout**: 20-second connection timeout
- **Behavior**: If Wi-Fi doesn't connect within 20 seconds, the script stops execution

### 2. LED Blink Function

- **Purpose**: Visual indicator for script status and API response
- **Success Response**: LED blinks 3 times quickly (200ms intervals) when API call succeeds
- **Failure Response**: LED stays on for 2 seconds when API call fails
- **Use Case**: Allows monitoring script status when ESP32 is connected to power supply without laptop connection

### 3. Data Transmission Function

- **Purpose**: Sends sensor data to the Django server
- **Data Payload**:
  - Timestamp (formatted as ISO string)
  - Device ID (`myesp`)
  - Random number (0-100)
  - JSON data (temperature: 25.5, pressure: 1013.25)
- **API Response Handling**:
  - Success: Triggers LED blink pattern
  - Failure: Triggers LED failure pattern
- **Execution**: Runs in infinite loop with 5-second intervals

---

## Django Server

### Architecture

- **Framework**: Django with Django REST Framework
- **Structure**: Single Django app (no dedicated app created)
- **API Endpoint**: Single POST endpoint for receiving IoT data
- **Data Viewing**: Django Admin Panel for data visualization

### Implementation Details

#### Models (`iot/models.py`)

- **IoTData Model**: Stores incoming sensor data
  - `device_tag`: Device identifier
  - `random_number`: Random integer (0-100)
  - `data`: JSON field for sensor readings
  - `timestamp`: Data timestamp
  - `created_at`: Auto-generated creation timestamp

#### Views (`iot/views.py`)

- **PingReciever**: ModelViewSet for handling POST requests
- **Philosophy**: Uses ViewSets for basic CRUD operations as they're more efficient for simple API structures
- **Methods**: Only allows POST requests

#### Serializers (`iot/serializers.py`)

- **IoTDataSerializer**: Simple ModelSerializer with all fields included
- **Design**: No field exclusions needed due to simple data structure

#### Admin Interface (`iot/admin.py`)

- **IoTDataAdmin**: Customized admin interface
- **Features**:
  - List display with key fields
  - Search functionality by device tag
  - Date filtering
  - Tabular data view

### Live Data Access

**Admin Panel URL**: https://iot.internal.ripeseed.io/admin/

**Login Credentials**:

- Username: `admin`
- Password: `admin`

**Data Access**:

1. Log in to the admin panel
2. Click on the "IoT" tab
3. View all transmitted data in tabular format
4. Real-time monitoring of ESP32 data transmission

The ESP32 has been running continuously for extended periods, providing real-time data for analysis and monitoring.

---

## API Endpoint

**POST** `https://iot.internal.ripeseed.io/iot/`

**Request Body**:

```json
{
  "device_tag": "myesp",
  "random_number": 42,
  "data": {
    "temperature": 25.5,
    "pressure": 1013.25
  },
  "timestamp": "2024-01-15T10:30:45Z"
}
```

**Response**: HTTP 201 on successful data storage
