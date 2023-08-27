# Thermo-Deformation Measurement (TDM) Platform Documentation

## Introduction
Welcome to the Thermo-Deformation Measurement (TDM) Platform: Redefining Precise Measurement.


<!doctype html>
<html>

<head>
	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
	<title>Setup Documentation</title>
	<link rel="stylesheet" href="assets/css/styles.css" type="text/css" />
	<meta name="viewport" content="width=device-width, minimum-scale=1.0, maximum-scale=1.0" />
</head>

<body>

	<section id="body" class="width">

		<aside id="sidebar" class="column-left">

			<header>
				<h1><a style="font-size: 22px" href="#">Setup Document</a></h1>
				<h2>Documentation by <b>Shox Computer</b></h2>
			</header>

			<nav id="mainnav">
				<ul>
					<li class="item selected-item"><a href="#topMain">Introduction</a></li>
					<li class="item"><a href="#HS">Help And Support</a></li>
					<li class="item"><a href="#DWT">Environment Setup</a></li>
					<li class="item"><a href="#HAP">Deploying the Web App</a></li>
					<li class="item"><a href="#AUC">Roles of Users</a></li>
					<li class="item"><a href="#bs">Handbook</a></li>
					
				</ul>
			</nav>
		</aside>
		<section id="content">
			<article id="topMain">
				<h2>1. Introduction</h2>
				<br>
				<p>Welcome to the Thermo-Deformation Measurement (TDM) Platform: Redefining Precise Measurement.</p>

				<p>Our TDM web application represents the pinnacle of innovation in the thermo-deformation measurement industry.
					Tailored for professionals, researchers, and enthusiasts alike, our platform encapsulates decades of expertise
					within an intuitive virtual space. With a focus on precision and user-friendliness, TDM provides an in-depth
					understanding of thermo-deformation measurement technology, products, and applications.</p>
			
				<p><strong>Explore Cutting-Edge Technology:</strong><br>
				In the "Technology" tab, immerse yourself in a realm of discovery. Explore various types of technology driving our platform, reshaping the way we measure and comprehend thermo-deformation across diverse industries.</p>
			
				<p><strong>Discover Our Product Range:</strong><br>
				The "Products" section is divided into two parts. Under "Systems," uncover our advanced machines designed to deliver real-time, accurate measurements. Then, delve into comprehensive features and descriptions of the products comprising these systems. Each product is a result of meticulous engineering, tailored to meet your most demanding measurement needs.</p>
			
				<p><strong>Experience Applications in Action:</strong><br>
				The "Applications" tab immerses you in the practical world of thermo-deformation measurement. Here, access videos illustrating processes in action, providing a clear view of how our solutions can benefit your industry.</p>
			
				<p><strong>Tailored Services:</strong><br>
				The "Services" section offers a range of solutions customized to your needs. Explore our services and stay up-to-date with our event calendar to ensure you never miss a learning or collaboration opportunity.</p>
			
				<p><strong>Stay Informed:</strong><br>
				In the "News" section, stay current with the latest updates from our company and the industry at large. Our platform serves as your reliable source for information and relevant trends.</p>
			
				<p><strong>Dive into Knowledge:</strong><br>
				Explore the "Blog" for in-depth insights, detailed analysis, and expert perspectives within the thermo-deformation measurement field. As a user, you have the ability to engage with content, give likes, and contribute new posts.</p>
			
				<p><strong>Connect with Us:</strong><br>
				The "Contact" section enables you to establish worldwide connections with our company. Find relevant contact information for your region and reach out to us to discuss collaborations, customized solutions, and more.</p>
			
				<p><strong>Personalized User Experience:</strong><br>
				Our platform offers three levels of access. "Customers" can explore the platform, add comments, and contribute to the blog. "Users" gain access to additional features such as downloading specific files and interacting with exclusive content. As an "Administrator," you have full control over the platform, from managing users and roles to overseeing files and events.</p>
			
				<p>At TDM, we are dedicated to excellence in thermo-deformation measurement and fostering a vibrant community of professionals. Join us on this exciting journey toward a world of precision measurement and transformative discoveries.</p>
			
				<p class="secondPara">Technologies Used in Web App are:</p>
				<ol class="expanded">
					<li>React.Js</li>
					<li>Redux</li>
					<li>Material UI</li>
					<li>MySQL Database</li>
					<li>Django Backend</li>
				</ol>
			</article>
			## Help And Support
			If you have any questions, please use the [WhatsApp Support](https://api.whatsapp.com/send?phone=50662558356&text=Company%3A%20TDM%2C%20I%20need%20support%20with%20the%20following%20issue%3A%20) for assistance.

			<article id="HS">
				<h2>2. Help And Support </h2><br/>
				<p>
					If you have any questions, please use the Contact us via WhatsApp for support:<br/>
					<a class="button" href="https://api.whatsapp.com/send?phone=50662558356&text=Company%3A%20TDM%2C%20I%20need%20support%20with%20the%20following%20issue%3A%20" target="_blank">WhatsApp Support</a>
				</p>
			</article>
			## Environment Setup
			Instructions to set up the development environment for TDM.

			<article id="DWT">
				<h2>3. Environment Setup</h2>
				<br>
				<p class="secondPara" style="margin-bottom:0px">To run the 2 Apps you need 5 things in your development
					machine as mentioned below.</p>
				<br>
				<p class="secondPara heading">A. Download NodeJs</p>
				<img height="100%" width="25%" src="assets/img/nodejs_logo.png" alt="HTML Structure" />

				<ol class="styledlist listCustom" type="I">
					<li>
						<ul> Download instructions
							<li>Mac users: For OS X, download the .pkg file form below link.<b>(v20.5.0 
									recommended)</b></li>
							<li>Windows users: Download either the MSI or the .exe form below link, whichever you prefer
								.<b>(v.20.5.0  recommended)</b></li>
						</ul>
						<a href="https://nodejs.org/dist/v20.5.0/" class="button" target="_blank">Download Node
							v.20.5.0 from here</a>
					</li>

					<li>After Installing NodeJs you'll most likely need to restart your computer.</li>
					<p style="color:#757575;font-size:18px;">To ensure that NodeJs is installed correctly, you can type:
					</p>
					<code class="codeBlockBg">
						node -v
				</code>
					</li>
					<p style="color:red;font-size:18px;">NOTE: DO NOT IGNORE THE NODE JS VERSION. IT HAS TO BE 20.5.x
					</p>

				</ol>
				<p class="secondPara heading" id="Configure">B. Install Git and Windows-Build-Tools if using <span style="color:red">Windows PC Only </span></p>

				<ul>
					<li> Download and install the latest from this link. https://git-scm.com/</li>
					<br>
					<li>Start PowerShell as Administrator and run
						<code class="codeBlockBg">
							npm install -g windows-build-tools
						</code> </li>
				</ul>

				<p class="secondPara heading" id="Configure">C. Install Tailwind</p>
				<img height="100%" width="30%" src="assets/img/tailwindcss.png" alt="HTML Structure" />
				<h4>In your command prompt, type: </h4>
				<code class="codeBlockBg">
					npm install -D tailwindcss
					</code>
				<h4>Follow step by step with official documentation <a href="https://tailwindcss.com/docs/installation">https://tailwindcss.com/docs/installation</a> </h4>
				<p class="secondPara heading" id="Configure">D. Install Yarn</p>
				<h4>In your command prompt, type: </h4>
				<code class="codeBlockBg">
						npm install -g yarn
					</code>

					<p class="secondPara heading" id="Configure">E. Install Django, Django Rest Framework, Corsheaders, and Creditor</p>

					<h4>1. Install Django</h4>
					<code class="codeBlockBg">
					pip install django
					</code>
					
					<h4>2. Install Django Rest Framework</h4>
					<code class="codeBlockBg">
					pip install djangorestframework
					</code>
					
					<h4>3. Install Corsheaders</h4>
					<code class="codeBlockBg">
					pip install django-cors-headers
					</code>
					
					<h4>4. Install Creditor</h4>
					<code class="codeBlockBg">
					pip install creditor
					</code>
					
					<p>Now that you have installed the necessary packages, you can proceed with the following steps to set up Firebase:</p>
					
					<p>Remember to replace the placeholders with your actual configurations.</p>
					
			</article>
			## Deploying the Web App
			Information on deploying the TDM web application.

			<article id="InstallDjangoReact">
				<h2>4. Installing Django and React App</h2>
				<br>
				<p><b><u> Step 1:</u></b> Create Project Folder</p>
				<code class="codeBlockBg">
					mkdir your_project_name
					cd your_project_name
				</code>
				<br>
				<p><b><u> Step 2:</u></b> Set Up Virtual Environment</p>
				<code class="codeBlockBg">
					python -m venv venv
					<br/> source venv/bin/activate  <br/> venv\Scripts\activate # On Windows: 
				</code>
				<br>
				<p><b><u> Step 3:</u></b> Install Django and set up a project.</p>
				<code class="codeBlockBg">
					pip install django
				</code>
				<br>
				<p><b><u> Step 4:</u></b> Create Frontend Folder</p>
				<code class="codeBlockBg">
					mkdir your_project_name
					cd your_project_name
				</code>
				<p><b><u> Step 5:</u></b> Install necessary packages for React.</p>
				<code class="codeBlockBg">
					cd frontend
					yarn install 
				</code>
				<br>
				<p><b><u> Step 6:</u></b> Configure Django settings for frontend and backend communication.</p>
				<code class="codeBlockBg">
					# backend/settings.py
					<br/> <br/>
					ALLOWED_HOSTS = ['jompy31.pythonanywhere.com','127.0.0.1']  Adjust as needed 
					<br/> <br/>
					CORS_ALLOW_ALL_ORIGINS = True  # Adjust as needed for security
					<br/> <br/>
					INSTALLED_APPS = [
						# ... other apps ...
						'corsheaders',
					]
					<br/> <br/>
					MIDDLEWARE = [
						# ... other middleware ...
						'corsheaders.middleware.CorsMiddleware',
					]
					<br/> <br/>
					DATABASES = {
						'default': {
							'ENGINE': 'django.db.backends.mysql',
							'NAME': 'Example$TDM',
							'USER': 'Example',
							'PASSWORD': 'Example',
							'HOST':'Example.mpysql.server.com',
							'PORT': '',
						}
					}
					<br/> <br/>
					STATIC_URL = '/static/'
					STATICFILES_DIRS = ['/home/Example/backend_django/static']
					STATIC_ROOT = 'home/Example/static/'
					MEDIA_URL = '/media/'
					MEDIA_ROOT = '/home/Example/media/'
					<br/> <br/>
					EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
					EMAIL_HOST = 'smtpout.secureserver.net'
					EMAIL_PORT = 465  
					EMAIL_HOST_USER = 'example@example.com'
					EMAIL_HOST_PASSWORD = 'examplepasword'
					EMAIL_USE_SSL = True 

				</code>
				<br>
				<p><b><u> Step 7:</u></b> Configure the frontend to communicate with the backend.</p>
				<code class="codeBlockBg">
					// frontend\src\services\files.js
					<br/>
					//finalizado\src\services\products.js
					<br/>
					//finalizado\src\services\todos.js
					<br/><br/>
					Example<br/><br/>
					import axios from 'axios';

					const api = axios.create({
						baseURL: 'http://localhost:8000',  // Adjust the URL based on your backend setup
					});

					export default api;
				</code>
				<br>
				<p><b><u> Step 8:</u></b> Run the development servers for both frontend and backend.</p>
				<code class="codeBlockBg">
					
					python manage.py runserver  # In the main project directory
					<br>
					
					yarn start  # In the frontend directory
				</code>
				<br>
				<p>Now you have successfully set up a Django backend with a React frontend. You can further customize and build your application using these frameworks.</p>
			</article>

			
			<br>
			<a href="#topMain" class="arrowTop">
				<img src="assets/img/top.png" alt="gototop" />
			</a>

			<footer class="clear">
				<hr>
				<p>&copy; 2023 SHOX COMPUTER. &nbsp;| Developed by <a
						href="">Shox Computer </a></p>
			</footer>
			<article id="HAP">
				<h2>4. Deploying the Web App</h2>
				<br>
					<h3>Application Sections Overview:</h3>
					<p>Upon running the deployed application, you'll find the following sections:</p>

					<h4>1. Home Icon - /home</h4>
					<p>Clicking on the TDM icon will take you to the homepage.</p>
					<img src="assets/img/tdm_home.PNG" alt="Home Icon" width="40%" height="auto">

					<h4>2. Technology - /technology</h4>
					<p>This section provides an in-depth explanation of the applied technology.</p>
					<img src="assets/img/TDM_Technology.PNG" alt="Technology" width="40%" height="auto">

					<h4>3. Products and Applications - /products</h4>
					<p>Explore our range of products and applications.</p>
					<img src="assets/img/TDM_products.PNG" alt="Products" width="40%" height="auto">

					<h4>4. Services and Events Calendar - /services</h4>
					<p>Discover the services we offer and stay updated with our events calendar.</p>
					<img src="assets/img/TDM_services.PNG" alt="Services" width="40%" height="auto">
					<img src="assets/img/TDM_services1.PNG" alt="Services" width="40%" height="auto">

					<h4>5. Latest News - /news</h4>
					<p>Stay informed with the latest news updates.</p>
					<img src="assets/img/TDM_news.PNG" alt="News" width="40%" height="auto">

					<h4>6. Blog - /blog</h4>
					<p>Engage with our user community through our blog.</p>
					<img src="assets/img/TDM_blog.PNG" alt="Blog" width="40%" height="auto">

					<h4>7. Contact and Distributors - /contact</h4>
					<p>Connect with distributors and access the login button to sign in.</p>
					<img src="assets/img/TDM_contact2.PNG" alt="Contact" width="40%" height="auto">
					<img src="assets/img/TDM_contact1.PNG" alt="Contact" width="40%" height="auto">

					<h4>8. Login - /login</h4>
					<p>Connect with database to authenticated and use the specific rol of users.</p>
					<img src="assets/img/TDM_login.PNG" alt="Contact" width="40%" height="auto">

					<h4>9. Signup - /signup</h4>
					<p>Create a new User with Customer Rol and send email to administrator.</p>
					<img src="assets/img/TDM_Signup.PNG" alt="Contact" width="40%" height="auto">

					<h4>10. Forget Password - /reset_password</h4>
					<p>If you have access and forget the password you can get access following instructions</p>
					<img src="assets/img/TDM_forgetpassword.PNG" alt="Contact" width="40%" height="auto">
					<img src="assets/img/TDM_resetpassword.PNG" alt="Contact" width="40%" height="auto">
				</article>
				## User Roles and Functions
				Detailed explanation of different user roles and their functions.
				
			<article id="AUC">
				<h2>6. User Roles and Functions</h2>
				<br>
				<p>When accessing the application through a web browser, different user roles have distinct functions and capabilities. Here's a breakdown of the user roles and their respective functions:</p>
				
				<h3>6.1. Customer User</h3>
				<p>The Customer user is the target audience for the products and services provided by the application. Upon accessing the application, the Customer can:</p>
				<ul>
					<li>Browse and explore the product catalog.</li>
					<li>View detailed product descriptions, images.</li>
					<li>Learn about the application's various services and their benefits.</li>
					<li>Stay informed about the latest news and updates through the blog section.</li>
					<li>Contact distributors and initiate business inquiries.</li>
					<li>Access event schedules and register for upcoming events.</li>
					<img width="50%" src="assets/img/TDM_calendar.PNG" alt="Calendar" /><br>
				</ul>

				<h3>6.2. Technology User</h3>
				<p>The Technology user is focused on exploring and learning about the technological aspects of the system. This user role is directed towards:</p>
				<ul>
					<li>Accessing to files upload by administrator user.</li>
					<img width="50%" src="assets/img/TDM_files.PNG" alt="Files" /><br>
					<li>Browse and explore the product catalog.</li>
					<li>View detailed product descriptions, images.</li>
					<li>Learn about the application's various services and their benefits.</li>
					<li>Stay informed about the latest news and updates through the blog section.</li>
					<li>Contact distributors and initiate business inquiries.</li>
					<li>Access event schedules and register for upcoming events.</li>
					<img width="50%" src="assets/img/TDM_calendar.PNG" alt="Calendar" /><br>
				</ul>

				<h3>6.3. Admin User</h3>
				<p>The Admin user plays a central role in managing and overseeing the entire system. Upon accessing the application, the Admin is prompted to submit their mobile number for authentication.</p>
				<img width="50%" src="assets/img/TDM_current_user.PNG" alt="Authentication" /><br>
				<img width="50%" src="assets/img/TDM_sidebar.PNG" alt="Admin Authentication" /><br>
				<p>After successful authentication, the Admin gains access to the Admin Dashboard. Here, they have various functions and capabilities:</p>
				<ul>
					<li><strong>Manage Team:</strong> The Admin can register new users with their respective roles. They can download the list of users in CSV format. Additionally, there's a search feature to find users by name, email, or staff status. A table displays current users, and the Admin can edit or delete users as needed.</li>
					<img width="50%" src="assets/img/TDM_adminuser.PNG" alt="Manage Users" />
					<img width="50%" src="assets/img/TDM_adminregister.PNG" alt="Register Users" />
					<img width="50%" src="assets/img/TDM_adminuseredit.PNG" alt="Register Users" /><br>
					<li><strong>Administer Customers:</strong> The Admin can add new customers, including their name, email, description, priority (low, medium, high), status (new, contacted, winner), and phone number. This function enables effective customer relationship management. Admins can also add comments related to customer interactions.</li>
					<img width="50%" src="assets/img/TDM_Customer.png" alt="Manage Customers" />
					<img width="50%" src="assets/img/TDM_admincustomer1.PNG" alt="Manage Customers" />
					<img width="50%" src="assets/img/TDM_admincustomer2.PNG" alt="Manage Customers" /><br>
					<li><strong>Administer Files:</strong> The Admin can add, delete, search, and download files to share with users having the "user" role. This feature enhances file management and collaboration.</li>
					<img width="50%" src="assets/img/TDM_adminfiles.PNG" alt="Manage Files" /><br>
					<li><strong>Administer Calendar:</strong> Events can be added and removed from the calendar. These events are visible to other roles as well. Admins can select specific events and send email notifications to relevant parties to keep them informed.</li>
					<img width="50%" src="assets/img/TDM_services1.PNG" alt="Manage Calendar" /><br>
					<li><strong>Administer Blog:</strong> The Admin can view, edit, and delete all existing blog posts. This function ensures complete control over the content presented in the blog section.</li>
					<img width="50%" src="assets/img/TDM_adminblog.PNG" alt="Manage Blog" /><br>
					<li><strong>Administer Media Website:</strong> Here, the Admin can customize the images and properties of the seven navigation tabs (Home, Technology, Products, Applications, Services, News, Contacts).</li>
					<img width="50%" src="assets/img/TDM_adminmedia.PNG" alt="Manage Media Website" /><br>
				</ul>
				<p>The Admin Dashboard provides comprehensive tools for managing different aspects of the application and ensuring a seamless user experience.</p>

				
				<p>By tailoring user roles and functions, the application offers a seamless experience to individuals with different responsibilities and interests.</p>
			</article>

			## User Handbook
			Step-by-step guide on using various features and functions of the application.
			
			<article id="bs">
				<h2>7. User Handbook</h2>
				
				<p>This section provides a step-by-step guide on how to use the various features and functions of the application.</p>
				
				<h3>7.1. Login and User Authentication</h3>
				<p>Upon accessing the application, users are presented with the login page. Here, users can authenticate using their email and password.</p>
				<img width="50%" src="assets/img/TDM_login.PNG" alt="Login Page" /><br>
				<p>For new users, the "Sign Up" button allows registration with the "customer" role. The "Forgot Password" button enables users to request a password reset via their registered email.</p>
				<img width="50%" src="assets/img/TDM_Signup.PNG" alt="Signup Page" /><br/>
				<img width="80%" src="assets/img/TDM_forgetpassword.PNG" alt="Signup Page" /><br>
				<p>After successful authentication, the "Login" button transforms into a dropdown displaying the user's email. Clicking the dropdown reveals personalized options based on the user's role:</p>
				<ul>
					<li><strong>Customer Role:</strong> Access to the Calendar, Profile, and Logout.</li>
					<li><strong>User Role:</strong> Access to Calendar, Files, Profile, and Logout.</li>
					<li><strong>Admin Role:</strong> Access to Calendar, Files, Users, Profile, Logout, and Admin Sidebar.</li>
				</ul>
				
				<h3>7.2. Admin Sidebar and User Management</h3>
				<p>Admin users have an additional "Admin Sidebar" option. Clicking on it opens a sidebar with options for managing various aspects of the application:</p>
				<img width="50%" src="assets/img/TDM_adminsidebar.PNG" alt="Admin Sidebar" /><br/>
				<img width="10%" src="assets/img/TDM_adminsidebar1.PNG" alt="Admin Sidebar" /><br>
				<p>Admin users can:</p>
				<ul>
					<li><strong style="font-size: 200%;">Administer user roles, including creating and managing users.</strong></li><br><br><br>
					<img width="20%" src="assets/img/TDM_USERADMIN.png" alt="Admin Sidebar" />
					<img width="80%" src="assets/img/TDM_USER1.PNG" alt="Admin Sidebar" />
					<img width="80%" src="assets/img/TDM_USER2.PNG" alt="Admin Sidebar" />
					<img width="60%" src="assets/img/TDM_adminuseredit.PNG" alt="Admin Sidebar" />
					<li><strong style="font-size: 200%;">Add, delete, search, and download customer database.</strong></li><br><br><br>
					<img width="20%" src="assets/img/TDM_CustomerADMIN.png" alt="Admin Sidebar" />
					<img width="80%" src="assets/img/TDM_admincustomer.PNG" alt="Admin Sidebar" />
					<img width="60%" src="assets/img/TDM_Customer1.png" alt="Admin Sidebar" />
					<img width="60%" src="assets/img/TDM_Customer2.png" alt="Admin Sidebar" />
					<img width="50%" src="assets/img/TDM_Customer3.png" alt="Admin Sidebar" />
					<li><strong style="font-size: 200%;">Add, delete, search, and download files.</strong></li><br><br><br>
					<img width="20%" src="assets/img/TDM_FilesADMIN.png" alt="Admin Sidebar" />
					<img width="80%" src="assets/img/TDM_adminfiles.PNG" alt="Admin Sidebar" />
					<li style="font-size: 200%;"><strong>Manage event schedules and calendars.</strong></li><br><br><br>
					<img width="20%" src="assets/img/TDM_CalendarADMIN.png" alt="Admin Sidebar" />
					<img width="80%" src="assets/img/TDM_Calendar1.png" alt="Admin Sidebar" />
					<img width="60%" src="assets/img/TDM_Calendar2.png" alt="Admin Sidebar" />
					<img width="60%" src="assets/img/TDM_Calendar3.png" alt="Admin Sidebar" />
					<li style="font-size: 200%;"><strong>Create and publish news and blog posts.</strong></li><br><br><br>
					<img width="20%" src="assets/img/TDM_BlogADMIN.png" alt="Admin Sidebar" />
					<img width="80%" src="assets/img/TDM_blog1.PNG" alt="Admin Sidebar" />
					<img width="60%" src="assets/img/TDM_blog2.PNG" alt="Admin Sidebar" />
					<img width="90%" src="assets/img/TDM_blog3.PNG" alt="Admin Sidebar" />
					<li><strong  style="font-size: 200%;">Manage media.</strong></li><br><br><br>
					<img width="20%" src="assets/img/TDM_MediaADMIN.png" alt="Admin Sidebar" />
					<img width="80%" src="assets/img/TDM_Media.png" alt="Admin Sidebar" />
					<img width="90%" src="assets/img/TDM_Media1.png" alt="Admin Sidebar" />
					<img width="90%" src="assets/img/TDM_Media2.PNG" alt="Admin Sidebar" />
					<img width="90%" src="assets/img/TDM_Media3.PNG" alt="Admin Sidebar" />
					<img width="60%" src="assets/img/TDM_Media4.PNG" alt="Admin Sidebar" />
					<img width="60%" src="assets/img/TDM_Media5.PNG" alt="Admin Sidebar" />
					<img width="60%" src="assets/img/TDM_Media6.PNG" alt="Admin Sidebar" />
					<img width="90%" src="assets/img/TDM_Media7.PNG" alt="Admin Sidebar" />
					<img width="90%" src="assets/img/TDM_Media8.PNG" alt="Admin Sidebar" />
					<img width="90%" src="assets/img/TDM_Media9.PNG" alt="Admin Sidebar" />
					<img width="60%" src="assets/img/TDM_Media10.PNG" alt="Admin Sidebar" />
					<img width="80%" src="assets/img/TDM_Media11.PNG" alt="Admin Sidebar" />
					<img width="60%" src="assets/img/TDM_Media12.PNG" alt="Admin Sidebar" />

				</ul>
			</article>
			<br></br>
			
			<br>
			<a href="#topMain" class="arrowTop">
				<img src="assets/img/top.png" alt="gototop" />
			</a>
			## Contact
			For any further inquiries, please feel free to [contact us](https://your_contact_link_here).

			<p>
				If you have any questions, please use the Contact us via WhatsApp for support:<br/>
				<a class="button" href="https://api.whatsapp.com/send?phone=50662558356&text=Company%3A%20TDM%2C%20I%20need%20support%20with%20the%20following%20issue%3A%20" target="_blank">WhatsApp Support</a>
			</p>

			<footer class="clear">
				<hr>
				<p>&copy; 2023 Shox Computer. Developed by <a
						href="">Shox Computer </a></p>
			</footer>

		</section>
		<div class="clear"></div>
	</section>


	<script>
		var header = document.getElementById("mainnav");
		var btns = header.getElementsByClassName("item");
		for (var i = 0; i < btns.length; i++) {
			btns[i].addEventListener("click", function () {
				var current = document.getElementsByClassName("selected-item");
				current[0].className = current[0].className.replace(" selected-item", "");
				this.className += " selected-item";
			});
		}
	</script>
</body>

</html>


&copy; 2023 Shox Computer. Developed by [Shox Computer]
