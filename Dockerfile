# ---- build stage ----
FROM python:3.12-slim AS build
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt
COPY . .

# ---- run stage ----
FROM python:3.12-slim
WORKDIR /app
ENV PATH=/root/.local/bin:$PATH
COPY --from=build /root/.local /root/.local
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
