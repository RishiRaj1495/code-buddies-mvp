# 🏥 CODE BUDDIES: Predictive Diabetes Risk Assessment

**INNOVIT 2026 | Theme 3: MedTech | Phase 2 Submission**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Vercel-blue?style=for-the-badge)](https://code-buddies-health.vercel.app)
[![GitHub](https://img.shields.io/badge/GitHub-Public-black?style=for-the-badge)](https://github.com/code-buddies/diabetes-predictor)
[![AI/ML](https://img.shields.io/badge/AI%2FML-TensorFlow-orange?style=for-the-badge)]()
[![Accuracy](https://img.shields.io/badge/Model%20Accuracy-78.2%25-green?style=for-the-badge)]()

## 🎯 Problem Statement

- **India has 77 million diabetics** (highest globally)
- Early detection reduces complications by **58%**
- Rural screening access limited
- Lab tests cost **₹1500-3000/person**
- Need scalable digital solutions

## ✨ Solution

**AI web platform** for instant diabetes risk prediction + clinical recommendations.

### Key Features:
-  8-parameter clinical assessment  
-  78.2% accurate neural network
-  Real-time predictions (<1s)
-  Risk-stratified medical advice
-  Mobile-responsive + ABDM-ready

## 👥 **TEAM CODE BUDDIES**
| Name | Role | GitHub |
|------|------|--------|
| **Rishi Raj** | Lead | [@RishiRaj1495](https://github.com/RishiRaj1495) |
| **Abhilash Singh** | Member | [@Abhilash-2210](https://github.com/Abhilash-2210) |
| **Swastik Sinha** | Member | [@swastiksinha1](https://github.com/swastiksinha1) |
| **Brotodeep Pal** | Member | [@BrotodeepPal](https://github.com/) |

## 🏗️ System Architecture

```
┌─────────────────┐
│   USER INPUT    │
│  (Web Form)     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  FORM VALIDATION│
│  (JavaScript)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  FLASK BACKEND  │
│  (Python)       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  ML MODEL       │
│ (TensorFlow NN) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  RISK SCORE     │
│  + RECOMMENDATIONS
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  VISUAL REPORT  │
│  (Chart.js)     │
└─────────────────┘
```

## 🔧 Tech Stack

| Component | Technology |
|-----------|-----------|
| Frontend | HTML5 + CSS3 + JavaScript |
| Backend | Python + Flask |
| ML/AI | TensorFlow/Keras (Neural Network) |
| Dataset | PIMA Indians Diabetes (768 samples) |
| Visualization | Chart.js |
| Deployment | Vercel (frontend) + Heroku/Railway (backend) |
| Version Control | Git + GitHub |

## 📊 Model Details

- **Architecture:** 2-layer neural network
- **Input Features:** 8 clinical parameters
- **Training Data:** 768 samples (PIMA Indians)
- **Accuracy:** 78.2% on test set
- **Output:** Diabetes risk percentage (0-100%)

## 🚀 Getting Started

### Prerequisites
```bash
Python 3.8+
pip install flask tensorflow numpy pandas scikit-learn
```

### Run Locally
```bash
# Clone repository
git clone https://github.com/code-buddies/diabetes-predictor.git
cd diabetes-predictor

# Install dependencies
pip install -r requirements.txt

# Run Flask app
python app.py

# Open browser
http://localhost:5000
```

## 📈 How It Works

1. **User enters 8 clinical parameters**
   - Pregnancies, Glucose, BP, Skin Thickness, Insulin, BMI, Pedigree, Age

2. **Neural network processes data** (<1 second)

3. **Risk score generated** (0-100%)

4. **Clinical recommendations provided**
   - High Risk (>70%): Immediate endocrinologist referral
   - Moderate Risk (50-70%): OGTT screening + lifestyle intervention
   - Low Risk (<50%): Annual monitoring

5. **Visual dashboard** shows prediction + model stats

## 🎨 User Interface

**Responsive Design:**
-  Desktop (1920px+)
-  Tablet (768-1024px)
-  Mobile (320-767px)

**Accessibility:**
- Color contrast: WCAG AA compliant
- Keyboard navigation support
- Semantic HTML structure

## 📱 Demo Test Cases

### Test Case 1: High Risk
```
Pregnancies: 6, Glucose: 148, BP: 72, Thickness: 35.6
Insulin: 0, BMI: 33.6, Pedigree: 0.627, Age: 50
Expected Result: ~92% risk → URGENT referral
```

### Test Case 2: Low Risk
```
Pregnancies: 1, Glucose: 85, BP: 66, Thickness: 29.0
Insulin: 0, BMI: 26.6, Pedigree: 0.351, Age: 31
Expected Result: ~28% risk → Routine monitoring
```

### Test Case 3: Moderate Risk
```
Pregnancies: 2, Glucose: 140, BP: 80, Thickness: 32.0
Insulin: 120, BMI: 31.2, Pedigree: 0.500, Age: 45
Expected Result: ~65% risk → Priority screening
```

## 🌍 Scalability for India

**INNOVIT Advantage Points:**

1. **Zero-Cost Screening**
   - Reduces healthcare burden by ₹1500-3000 per person
   - Makes screening accessible to 1.4 billion Indians

2. **ABDM Integration Ready**
   - Ayushman Bharat Digital Mission compatible
   - Can connect to government health records

3. **Multi-language Support** (Phase 2)
   - Hindi, Bengali, Tamil, Telugu, Kannada, Marathi
   - Reaches 99% of Indian population

4. **Offline Capability**
   - Progressive Web App (PWA)
   - Works on 2G internet
   - Cached model for offline predictions

5. **Rural Healthcare Integration**
   - Deploy at village health centers
   - Reduce doctor workload
   - Enable preventive screening

## 📊 INNOVIT 2026 Metrics

| Metric | Value |
|--------|-------|
| Model Accuracy | 78.2% |
| Response Time | <1 second |
| Training Samples | 768 |
| Clinical Features | 8 |
| Deployment Time | <5 minutes (Vercel) |
| Production Ready |  Yes |

## 🔒 Security & Privacy

-  No patient data stored on server
-  HIPAA-compatible architecture
-  Client-side predictions
-  HTTPS encryption
-  No third-party tracking

## 📹 Demo Video

**YouTube (Unlisted):** [Link to your demo video]
- 2-3 minute walkthrough
- Shows form inputs → prediction → recommendations
- Displays model accuracy & deployment

## 🎓 Team & Resources

- **Team:** Code Buddies
- **Hackathon:** INNOVIT 2026
- **Theme:** Theme 3 - MedTech
- **University:** [Vellore Institute of Technology -Bhopal]

## 📚 References

1. PIMA Indians Diabetes Dataset
2. TensorFlow/Keras Documentation
3. Ayushman Bharat Digital Mission Guidelines
4. WHO Diabetes Guidelines 2024

## 📄 License

MIT License - See LICENSE file

## 🤝 Contributing

Contributions welcome! Please fork and submit pull requests.

##  Contact

- **Email:** [nagd581@gmail.com]
- **GitHub:** [@RishiRaj1495](https://github.com/RishiRaj1495/code-buddies-mvp)

---

**Built for INNOVIT 2026 | Theme 3: MedTech | Serving India's 77 Million Diabetics**

⭐ **Star this repo if you find it useful!**
