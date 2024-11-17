# A simple flask project that summarizes financial documents using Google's Generative API(gemini).
---

## **Features**  

1. **Document Summarization:**
   - Parses and summarizes key insights from financial documents such as reports, balance sheets, and more.  

2. **Flask API:**  
   - Exposes RESTful endpoints for uploading and summarizing documents.  

3. **CI/CD on AWS ECS:**  
   - Automates the build, test, and deployment processes using:
     - **AWS ECS**: For running containerized applications.  
     - **GitHub Actions**: For CI/CD workflows.  

4. **Scalability:**  
   - Deployed on AWS ECS with scalability and reliability through load balancing and auto-scaling.  

---
**Key Steps in CD:**  
1. Authenticate with AWS.
2. Build and push the Docker image to Docker hub
3. Build and push the Docker image to ECR.  
4. Update the ECS service to use the new image.  

---


## **AWS ECS Deployment**  

### **Infrastructure Overview:**  
1. **ECS Cluster:** Manages the containerized application.  
2. **ECR:** Stores Docker images for deployment.  
4. **Task Definition:** Configures how the containers run.  

### **Deploying Updates:**  
1. Push changes to the `main` branch.  
2. GitHub Actions automatically triggers the `deploy.yml` workflow.  
3. The updated application is deployed to AWS ECS.  

---

[](./github_actions_workflow.png)
