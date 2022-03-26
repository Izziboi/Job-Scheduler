<h1><p align="center">Job Scheduler App With Python Tkinter</p></h1>

## Introduction
<p align="justify">
I once worked with a very nice dude who was a freelance gardener. He was very articulate with record-keeping and this he achieved using a large notebook. He often checked the notebook to know his next job schedule and consequently plan for it. Information concerning his jobs included the name of his client, their address, phone number, date of job, etc. While this was a nice practice, it happened that there was a tiny challenge - checking the records while on transit. He had to struggle between driving and turning the pages of the notebook. When I observed this, I thought of the possibility of making these information available on the go - that is, on mobile devices. As a result, I decided to apply my knwledge of python to create an app that can address this challenge as much as possible. Hence this work.
</p>

## About the App
<p align="justify">
The app has the following sections:<br>
- The Login: This is the first port of call where a user enters their login details (please see below). If the correct details are logged in, the app opens the section for viewing the schedules.
  
![image](https://user-images.githubusercontent.com/44449730/160242100-46f70058-5c1e-415a-9ccc-75d94df38099.png)

- The Login Editor: Here a user can edit the login particulars by entering the old ones and then the new ones (please see below). The app replaces the old particulars with the new ones.
  
![image](https://user-images.githubusercontent.com/44449730/160242177-6e2343d3-6eca-441d-bcf5-d725e4197862.png)

- The Record Editor: This page is used to edit already existing records or job schedules (please see below). At the top, the user enters the customer name and job date they want to change and then the new information to add, below. Only the information to add are required in the fields below.
  
![image](https://user-images.githubusercontent.com/44449730/160242601-84a1703d-3956-4e0a-b7a8-c11e25cc099e.png)

- The Record Viewer: On this page, the user can view any schedule or record of their choice based on filtering choice (see below). The filtering parameters are customer name and job date.
  
![image](https://user-images.githubusercontent.com/44449730/160242928-4707b0cb-5642-4ced-99f9-8556b6824feb.png)

</p>

## How to Use the App
<p align="justify">
A user logs in with the correct login details and the record viewer page opens. If the wrong detail(s) is/are entered, the system pops up an error box. On the login and record viewer pages, the user can click on the 'Edit Login Details' button to edit the login particulars.<br>
When on the record viewer page the user can input job date or customer name or both, to view the schedule against the input parameter. On clicking the 'View Schedule' button, the record(s) would display at the lower part of the page.<br>
Please note that the output record display is limited to 5 rows at this point in time. Increase in the number of rows is of course very possible.<br>
The user may wish to send the schedule to their email so they can carry them on their mobile device. In that case they only need to enter the recipient email address on the email field and click the 'To Email' button.<br>
Furthermore, they may wish to send the schedule as an sms to their phone. In that case, they just need to enter the recipient phone number (starting with plus sign and then the country code) and click the 'To Phone' button.<br>
Users may please explore other functionalities on the app, as they are very easy to understand.
</p>

## Result
<p align="justify">
The result is a display of the output of the records fetched. Below is a tabular display shown at the lower part of the record viewer page.
  
![image](https://user-images.githubusercontent.com/44449730/160243748-168adc37-0b46-4ee0-80df-fcc4749c1884.png)
  
As mentioned earlier, it can also deliver an email to a valid email address. Below is an email delivered by the app to a recipient.
  
![image](https://user-images.githubusercontent.com/44449730/160243992-6e9a9f0e-601c-4604-8a9b-baa1f401ffc5.png)


</p>
