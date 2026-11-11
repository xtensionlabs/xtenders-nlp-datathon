FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 HF_HOME=/opt/sauti/hf-cache OMP_NUM_THREADS=2 MKL_NUM_THREADS=2
WORKDIR /opt/sauti

COPY requirements-model.txt ./
RUN python -m pip install --no-cache-dir --index-url https://download.pytorch.org/whl/cpu "torch>=2.6,<3" \
    && python -m pip install --no-cache-dir -r requirements-model.txt "gdown>=5,<7" "tzdata>=2025.2"

COPY train_joint_intent_slot.py track_c_evaluation.py ./
COPY sauti/sauti.py sauti/sauti_model.py ./sauti/
COPY sauti/web/ ./sauti/web/
COPY models/track_c_final/metrics_and_errors.json ./models/track_c_final/
ARG TRACK_C_CHECKPOINT_ID
RUN test -n "$TRACK_C_CHECKPOINT_ID" \
    && gdown "$TRACK_C_CHECKPOINT_ID" -O models/track_c_final/best_model.pt \
    && python -c "from pathlib import Path; from sauti.sauti_model import load_responder; load_responder(Path('.'), Path('models/track_c_final/best_model.pt'))" \
    && chown -R 65534:65534 "$HF_HOME"

ENV HF_HUB_OFFLINE=1
USER 65534
EXPOSE 8000
CMD ["python", "sauti/sauti.py", "--repo", ".", "--checkpoint", "models/track_c_final/best_model.pt", "--host", "0.0.0.0", "--port", "8000"]
