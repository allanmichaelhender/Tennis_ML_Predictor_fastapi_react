# Tennis Match Predictor

I created this project to predict Men's ATP Tennis Matches. It using Machine Learning techniques and methods to imporve accuracy.

## Key Focus Areas
- Primary goal I achieved: Accurate predictions packaged in an easy to use and ligthweight application
- Unique value I provide: Simple user experience and up to date data + predictive models



## Live Demo

I've deployed a working version here:  
[Demo Site](https://tennis-predictor.freeddns.org/)





## My Tech Stack

**Frontend:**  
React · Vite  

**Backend:**  
Django · scikit-learn for ML Models 

**Database:**  
PostgreSQL  

**DevOps:**  
GitHub · AWS



## My Project Structure

Here's how I organized my code:


```
backend/
├── backend/          # Django settings/setup directory
├── api/              # Main application code
│   ├── ML_models/    # Machine Learning models and data

frontend/
├── src/              # Main source code
│   ├── pages/        # React Pages
│   ├── components/   # React Components
```




## Deployment

Here's how I deploy this project:

Frontend
1. Install dependencies: `npm install`
2. Build production version: `npm run build`
3. Deploy the `dist` folder to AWS (or other site)
4. Connect to Backend with VITE_API_URL environmental variable
5. Configure Nginx

Backend
1. Install dependencies: `pip install -r requirements.txt`
2. Connect database and provide DATABASE_URL environmental variable
3. Migrate and Collect Static with django
4. Configure Gunicorn
