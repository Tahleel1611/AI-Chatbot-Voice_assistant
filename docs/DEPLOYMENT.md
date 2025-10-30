# Deployment Guide

This guide covers various deployment options for the AI Chatbot Voice Assistant, from local development to production environments.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Local Development](#local-development)
- [Production Deployment](#production-deployment)
  - [Docker Deployment](#docker-deployment)
  - [Cloud Platforms](#cloud-platforms)
  - [VPS Deployment](#vps-deployment)
- [Configuration](#configuration)
- [Security Considerations](#security-considerations)
- [Monitoring and Maintenance](#monitoring-and-maintenance)
- [Troubleshooting](#troubleshooting)

---

## Prerequisites

### System Requirements

- **Operating System**: Windows 10+, macOS 10.14+, Ubuntu 18.04+
- **Python**: 3.8 or higher
- **RAM**: Minimum 4GB (8GB recommended for AI model)
- **Storage**: 2GB free space
- **Audio**: Microphone and speakers (for voice features)

### Software Dependencies

- Python pip
- Git (for cloning repository)
- Virtual environment tool (venv or virtualenv)
- (Optional) Docker for containerized deployment

---

## Local Development

### 1. Clone the Repository

```bash
git clone https://github.com/Tahleel1611/AI-Chatbot-Voice_assistant.git
cd AI-Chatbot-Voice_assistant
```

### 2. Set Up Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure Environment

```bash
# Copy example environment file
cp .env.example .env

# Edit .env with your settings (optional)
nano .env
```

### 5. Run the Application

**Voice Assistant Mode:**
```bash
python main.py
```

**Web API Mode:**
```bash
python app.py
```

The web interface will be available at `http://localhost:5000`

---

## Production Deployment

### Docker Deployment

Docker provides a consistent, isolated environment for deployment.

#### 1. Create Dockerfile

Create a `Dockerfile` in the project root:

```dockerfile
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    portaudio19-dev \
    python3-pyaudio \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create logs directory
RUN mkdir -p logs

# Expose Flask port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Run the application
CMD ["python", "app.py"]
```

#### 2. Create docker-compose.yml

```yaml
version: '3.8'

services:
  assistant:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
      - LOG_LEVEL=INFO
    volumes:
      - ./logs:/app/logs
      - ./config.toml:/app/config.toml
    restart: unless-stopped
```

#### 3. Build and Run

```bash
# Build the image
docker-compose build

# Run the container
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the container
docker-compose down
```

#### 4. Docker Hub Deployment

```bash
# Tag the image
docker tag ai-chatbot-voice-assistant:latest username/ai-assistant:latest

# Push to Docker Hub
docker push username/ai-assistant:latest

# Pull and run on any machine
docker pull username/ai-assistant:latest
docker run -p 5000:5000 username/ai-assistant:latest
```

---

### Cloud Platforms

#### Heroku Deployment

1. **Install Heroku CLI**

```bash
curl https://cli-assets.heroku.com/install.sh | sh
heroku login
```

2. **Create Heroku App**

```bash
heroku create your-app-name
```

3. **Create Procfile**

```
web: python app.py
```

4. **Configure Buildpacks**

```bash
heroku buildpacks:add heroku/python
```

5. **Set Environment Variables**

```bash
heroku config:set FLASK_ENV=production
heroku config:set LOG_LEVEL=INFO
```

6. **Deploy**

```bash
git push heroku main
heroku open
```

#### AWS EC2 Deployment

1. **Launch EC2 Instance**
   - Choose Ubuntu 20.04 LTS AMI
   - Select t2.medium or larger
   - Configure security group to allow port 5000
   - Launch and SSH into instance

2. **Setup on EC2**

```bash
# Update system
sudo apt-get update
sudo apt-get upgrade -y

# Install Python and dependencies
sudo apt-get install -y python3-pip python3-venv portaudio19-dev

# Clone repository
git clone https://github.com/Tahleel1611/AI-Chatbot-Voice_assistant.git
cd AI-Chatbot-Voice_assistant

# Setup virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
nano .env
```

3. **Setup Systemd Service**

Create `/etc/systemd/system/ai-assistant.service`:

```ini
[Unit]
Description=AI Chatbot Voice Assistant
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/AI-Chatbot-Voice_assistant
Environment="PATH=/home/ubuntu/AI-Chatbot-Voice_assistant/venv/bin"
ExecStart=/home/ubuntu/AI-Chatbot-Voice_assistant/venv/bin/python app.py
Restart=always

[Install]
WantedBy=multi-user.target
```

4. **Enable and Start Service**

```bash
sudo systemctl daemon-reload
sudo systemctl enable ai-assistant
sudo systemctl start ai-assistant
sudo systemctl status ai-assistant
```

5. **Setup Nginx Reverse Proxy**

```bash
# Install Nginx
sudo apt-get install -y nginx

# Configure Nginx
sudo nano /etc/nginx/sites-available/ai-assistant
```

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

```bash
# Enable site
sudo ln -s /etc/nginx/sites-available/ai-assistant /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

6. **Setup SSL with Let's Encrypt**

```bash
sudo apt-get install -y certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

#### Google Cloud Platform (GCP)

1. **Create VM Instance**

```bash
gcloud compute instances create ai-assistant \
    --image-family=ubuntu-2004-lts \
    --image-project=ubuntu-os-cloud \
    --machine-type=e2-medium \
    --zone=us-central1-a
```

2. **SSH and Setup**

```bash
gcloud compute ssh ai-assistant
# Follow EC2 setup steps
```

#### Microsoft Azure

1. **Create VM**

```bash
az vm create \
  --resource-group myResourceGroup \
  --name ai-assistant \
  --image UbuntuLTS \
  --admin-username azureuser \
  --generate-ssh-keys
```

2. **Configure and Deploy**
   - Follow similar steps as EC2 deployment

---

### VPS Deployment

For VPS providers like DigitalOcean, Linode, or Vultr:

1. **Create Droplet/Server**
   - Choose Ubuntu 20.04
   - Select appropriate size (2GB RAM minimum)

2. **Initial Server Setup**

```bash
# SSH into server
ssh root@your-server-ip

# Create non-root user
adduser aiassistant
usermod -aG sudo aiassistant

# Setup SSH key authentication
# Configure firewall
ufw allow OpenSSH
ufw allow 80/tcp
ufw allow 443/tcp
ufw enable
```

3. **Deploy Application**
   - Follow EC2 deployment steps

---

## Configuration

### Production Settings

Update `config.toml` for production:

```toml
[assistant]
name = "Friday AI"
version = "1.0.0"

[settings]
language = "en-in"
pause_threshold = 1.0
max_retries = 3
speech_timeout = 5

[logging]
level = "WARNING"  # Reduce verbosity in production

[security]
debug = false
```

### Environment Variables

Set production environment variables:

```bash
export FLASK_ENV=production
export FLASK_DEBUG=False
export LOG_LEVEL=WARNING
```

### Security Configuration

1. **Set Secret Key**

```python
# In app.py
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-here')
```

2. **Configure CORS**

```python
# In app.py
CORS(app, resources={
    r"/process-command": {
        "origins": ["https://your-domain.com"]
    }
})
```

3. **Enable HTTPS**
   - Use Let's Encrypt for SSL certificates
   - Configure Nginx/Apache for HTTPS

---

## Security Considerations

### Best Practices

1. **Keep Dependencies Updated**
```bash
pip list --outdated
pip install --upgrade package-name
```

2. **Use Environment Variables**
   - Never commit `.env` file
   - Use secrets management (AWS Secrets Manager, etc.)

3. **Implement Rate Limiting**

```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=get_remote_address)

@app.route('/process-command', methods=['POST'])
@limiter.limit("100 per hour")
def handle_command():
    # Your code
```

4. **Input Validation**
```python
from flask import request, jsonify

def validate_command(command):
    if not command or len(command) > 500:
        return False
    return True
```

5. **Secure Headers**

```python
from flask_talisman import Talisman

Talisman(app, content_security_policy=None)
```

### Firewall Configuration

```bash
# Allow only necessary ports
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow 'Nginx Full'
sudo ufw enable
```

---

## Monitoring and Maintenance

### Logging

Monitor application logs:

```bash
# Systemd service logs
sudo journalctl -u ai-assistant -f

# Application logs
tail -f logs/conversation_*.txt
```

### Health Checks

Create a health check endpoint:

```python
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200
```

### Monitoring Tools

- **Uptime Monitoring**: UptimeRobot, Pingdom
- **Error Tracking**: Sentry
- **Performance Monitoring**: New Relic, Datadog
- **Log Aggregation**: ELK Stack, Papertrail

### Backup Strategy

```bash
# Backup script
#!/bin/bash
BACKUP_DIR="/backup/ai-assistant"
DATE=$(date +%Y%m%d)

# Backup logs
tar -czf $BACKUP_DIR/logs-$DATE.tar.gz logs/

# Backup configuration
cp config.toml $BACKUP_DIR/config-$DATE.toml
cp .env $BACKUP_DIR/env-$DATE
```

---

## Troubleshooting

### Common Issues

1. **Port Already in Use**
```bash
# Find and kill process using port 5000
lsof -i :5000
kill -9 PID
```

2. **Permission Denied**
```bash
# Fix file permissions
chmod +x main.py app.py
```

3. **Module Not Found**
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

4. **Audio Device Not Found**
```bash
# Linux: Install PortAudio
sudo apt-get install portaudio19-dev

# macOS: Install PortAudio
brew install portaudio
```

### Performance Optimization

1. **Use Production WSGI Server**

```bash
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

2. **Enable Caching**
3. **Optimize Model Loading**
4. **Use CDN for Static Files**

---

## Scaling

### Horizontal Scaling

- Use load balancer (Nginx, HAProxy)
- Deploy multiple instances
- Implement session management

### Vertical Scaling

- Increase server resources
- Optimize code and queries
- Use faster storage (SSD)

---

## Support

For deployment issues:
- Check [Troubleshooting Guide](../README.md#troubleshooting)
- Open an issue on GitHub
- Review logs for error messages

---

## Additional Resources

- [Flask Deployment Options](https://flask.palletsprojects.com/en/2.0.x/deploying/)
- [Docker Documentation](https://docs.docker.com/)
- [AWS EC2 Guide](https://docs.aws.amazon.com/ec2/)
- [Nginx Configuration](https://nginx.org/en/docs/)
