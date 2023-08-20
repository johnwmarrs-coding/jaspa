# Stage 2: Run Flask API
FROM python:3.11-alpine
WORKDIR /app
COPY src/api/* .
RUN mkdir build
COPY src/ui/build ./build
# Install Python dependencies for Flask
RUN pip install --no-cache-dir -r requirements.txt

# Environment variables needed for Flask app
ENV FLASK_APP=app.py

# Expose the port the app runs on
EXPOSE 5000

# Serve both React UI and Flask API
CMD ["python", "app.py"]
