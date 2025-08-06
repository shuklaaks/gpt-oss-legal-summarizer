# GPT-OSS Legal Contract Summarizer

This repository provides a ready-to-use pipeline for running OpenAI's GPT‑OSS models locally (HPC / GPU workstations) or in Google Colab for reproducibility testing. The example use case demonstrates summarizing legal contracts and flagging compliance risks.

## Features
- Works with **GPT‑OSS‑20B** (default) or **GPT‑OSS‑120B** (larger capacity)
- Supports **TXT**, **CSV**, and **PDF** contract sources
- Runs locally or in **Google Colab**
- Enterprise-ready, with reproducible workflows

---

## Hardware Requirements

| Model         | Minimum Hardware                   | Recommended |
|---------------|------------------------------------|-------------|
| GPT‑OSS‑20B   | 2×A100 80GB or 4×RTX 4090           | HPC cluster |
| GPT‑OSS‑120B  | 8×A100 80GB                         | HPC cluster |

---

## Local Setup

```bash
# Clone repository
git clone https://github.com/shuklaaks/gpt-oss-legal-summarizer.git
cd gpt-oss-legal-summarizer

# Install dependencies
pip install -r requirements.txt

# Enable Git LFS for model weights
git lfs install

# Run the script
python scripts/gpt_oss_legal_summary.py
```

---

## Google Colab Execution (for Reproducibility)
Click below to open a GPU‑enabled Colab notebook with the same pipeline:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](
https://colab.research.google.com/github/YOUR_GITHUB_USERNAME/gpt-oss-legal-summarizer/blob/main/notebooks/gpt_oss_legal_summary.ipynb)

---

## Example Output
```
Summary:
- Vendor must comply with GDPR, CCPA, and similar privacy laws.
- Breaches must be reported within 72 hours.
- Approval required before transferring data outside approved jurisdictions.
- Client may terminate with 30 days' notice for compliance violations.

Risks:
- Possible data transfer violations.
- Tight breach reporting window may require strict monitoring.
```

---

## License
MIT License. See LICENSE file for details.

---

## Acknowledgements
- OpenAI for releasing GPT‑OSS models
- Hugging Face for Transformers library
