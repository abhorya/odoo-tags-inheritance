# Deployment Guide for Tags Inheritance Module

This guide will help you push your module to GitHub and then deploy it to Odoo.sh.

## Step 1: Push to GitHub

1. Create a new repository on GitHub:
   - Go to https://github.com/new
   - Name it `odoo-tags-inheritance` (or any name you prefer)
   - Choose "Private" if you want to keep your code private
   - Click "Create repository"

2. Add the GitHub repository as a remote:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/odoo-tags-inheritance.git
   ```
   (Replace `YOUR_USERNAME` with your GitHub username)

3. Push your code to GitHub:
   ```bash
   git push -u origin 18.0
   ```

## Step 2: Deploy to Odoo.sh

1. Go to https://www.odoo.sh/ and log in with your Odoo account.

2. Create a new project:
   - Click "New Project"
   - Enter a name for your project (e.g., "Tags Inheritance")
   - Select the Odoo version (18.0)
   - Click "Create"

3. Add your GitHub repository:
   - In your Odoo.sh project, go to "Branches"
   - Click "Add a branch"
   - Select "From external Git repository"
   - Enter your GitHub repository URL
   - Select the branch (18.0)
   - Click "Add"

4. Wait for the build to complete:
   - Odoo.sh will automatically build your module
   - You can check the build status in the "Builds" tab

5. Test your module:
   - Once the build is complete, click on the build
   - Click "Connect" to access the Odoo instance
   - Install your module from the Apps menu

## Step 3: Publish to Odoo App Store (Optional)

If you want to publish your module to the Odoo App Store:

1. Go to https://apps.odoo.com/
2. Click "Submit an App"
3. Fill in the required information
4. Upload your module as a ZIP file or provide the GitHub repository URL
5. Submit for review

## Notes

- Make sure your module follows Odoo's guidelines for the App Store if you plan to publish it.
- The price (€99.99) will be set during the App Store submission process.
- You may need to provide additional information or make changes based on the Odoo App Store review team's feedback.

## Support

If you encounter any issues during deployment, please contact:

- **Developer**: Sabry Youssef
- **Email**: vendorah2@gmail.com
- **Phone**: +20 1000059085 