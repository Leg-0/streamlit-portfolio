import streamlit as st
import pandas as pd
import os
from datetime import datetime
import plotly.graph_objects as go

st.set_page_config(initial_sidebar_state="expanded", layout="wide")
PHOTO_OF_ME = "assets/headshot_transparent.png"
WSU_LOGO = "assets/Wichita_State_University_logo.png"
SNOWFLAKE_LOGO = "assets/snowflake.png"

with st.sidebar:
    st.image(
        PHOTO_OF_ME,
        caption="Yep, that's me. You're probably wondering how I got here...",
    )
    st.header("About", text_alignment="center")
    st.write("""
    Born and raised in Kansas USA, I was encouraged to explore building things from a young age, including my very own PC when I was just 10 years old!
    Ever since then, I've had a deep love for anything modular, anything I can tweak to improve, even just slightly. Whether that be my computer, code, or even my car!
    I enjoy rock climbing, pickleball, spending time with friends, cooking, storytelling, and of course, building things. :wrench:
    """)

    if st.button("May I offer you balloons in these trying times?"):
        st.toast(":tada: Balloons! :tada:")
        st.balloons()


st.title("Aaron Isaacs", text_alignment="center")
st.caption("Full Stack Developer", text_alignment="center")

# region Experience
st.header("Experience", text_alignment="center")
SE, PE, DE = st.tabs(["Software Engineer", "Platform Engineer", "Data Engineer Co-op"])
with SE:
    st.subheader("Koch Capabilities, LLC", divider=True, text_alignment="center")
    st.subheader(
        "Data Management, Enablement, and Transformation team (D|MET)",
        text_alignment="center",
    )
    TPL, SWE = st.columns(2)
    with TPL:
        st.write("#### Technical Product Lead")
        st.write("""
            - Guiding Technology Path: Collaborating closely with data product owners (DPOs) my own technical product owner (TPO), and stakeholders, I am an active member in solving problems with technologies that would benefit the stakeholders and prevent major disruptions to our tech stack.
            - Subject Matter Expert: Any technical questions relating to our product (an internal streamlit webapp) are directed to me. Questions regarding connectivity, scalability, ease of transformation, and compatibility.
            - Delegated Feature Enhancements: While I still have an active hand in development, my expanded responsibilities require I take a more active part in delegating product enhancements to other engineers, and ensuring they have the resources and support they needed to be successful.
            - Lead Cross-Platform Spike: In an effort to engage and benefit one another, I planned, lead, and executed a spike with our Technology and our Security stacks to establish better access management mechanisms that both parties understood well and could manage easily.
            """)
    with SWE:
        st.write("#### Software Engineer")
        st.write("""
            - Created a data manipulation web application as part of a team of engineers for the Koch Tax organization using AWS microservices.
            - Working in an Agile environment, participating in bi-weekly stand-up calls, sprint planning, and retrospectives.
            - Collaborating with cross-functional teams to gather requirements and deliver high-quality software solutions.
            - Acting as the engineer liaison between the engineering capability and the security capability.
            - Greatly enhanced our build speed by developing D|MET-Specific python packages for services that didn't have an available Python SDK, such as dbt, and SigmaComputing.
            - Created and managed CI/CD workflows on Github Actions to automate testing and deployment of our applications.
            - Created the testing framework and pushing for engineers to use the requirements driven development (RDD) approach.
            - Created AI skill, prompt, and instructions files.
            """)

with PE:
    st.subheader(
        "Koch Ag. & Energy Solutions, LLC", divider=True, text_alignment="center"
    )
    st.subheader(
        "DevOps team",
        text_alignment="center",
    )
    st.write("""
- Optimized the patching process for large-scale Windows server environments, reducing downtime by several hours through the implementation of concurrency programming techniques integrated with robust CI/CD workflows in Jenkins and GitHub Actions.
  - Developed custom PowerShell scripts to automate comprehensive patching procedures, encompassing pre-patching health checks to ensure system stability, the core patching operations, and thorough post-patching validations to confirm successful updates.
  - Employed Python's Asyncio library to enable concurrent processing of patching tasks, significantly accelerating the overall process while utilizing subprocesses for seamless execution of PowerShell scripts.
  - Seamlessly integrated Jenkins for standard automated CI/CD pipelines, ensuring reliable and repeatable deployments.
  - Leveraged GitHub Actions for handling specialized, non-standard workflows that required custom logic and flexibility.
- Streamlined resource provisioning for development teams, eliminating hours of manual configuration by expertly setting up IAM permissions, EC2 instances, and secure network infrastructure via VPC and Route 53.
  - Configured precise IAM permissions tailored to the specific needs of each development team, ensuring secure and efficient access to AWS resources.
  - Provisioned EC2 instances with optimal configurations to meet performance and scalability requirements.
  - Managed comprehensive network security through VPC setups and Route 53 configurations, safeguarding data and applications.
- Enhanced security posture for new AWS accounts by implementing proactive vulnerability prevention measures, including detailed VPC subnet configurations, security group definitions, and route table setups.
  - Established VPC subnets to achieve secure network segmentation, isolating resources and minimizing potential attack surfaces.
  - Defined security groups with granular rules to meticulously control inbound and outbound traffic, adhering to best practices.
  - Configured route tables to facilitate proper routing within the VPC, ensuring efficient and secure data flow.
  - Deployed VPN instances in new accounts, fully compliant with Koch's stringent security and compliance standards.
        """)

with DE:
    st.subheader("Georgia-Pacific, LLC", divider=True, text_alignment="center")
    st.subheader(
        "Data Engineering team",
        text_alignment="center",
    )
    st.write("""
- Designed and implemented automated data migration workflows with AWS services including Lambda, S3, Redshift, and Aurora, combining cloud-native orchestration with Pandas-based transformation logic to improve reliability, scalability, and data quality across the pipeline.
- Led development of a proactive data pipeline monitoring and observability platform using REST API integration and Docker containerization, providing the team with faster failure detection, clearer pipeline health insights, and a stronger operational foundation.
- Supported the end-to-end creation of a proof-of-concept database solution, enforcing schema integrity with attribute constraints and building stored procedures and triggers to automate business rules while maintaining consistent data behavior.
        """)
# endregion
st.divider()

# region Certifications
st.header("Certifications", text_alignment="center")
cert_logo, cert, date = st.columns([1, 20, 2])
with cert_logo:
    st.image(SNOWFLAKE_LOGO, width=45)

with cert:
    st.write("""
        #### Snowflake Snow Pro Core Certification
    """)

with date:
    st.write("June 2025")


# endregion

st.divider()

# region Skills
st.header("Skills", text_alignment="center")
AWS, Soft, Lang, Other = st.tabs(["AWS", "Soft", "Languages", "Other"])

with AWS:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.badge("S3", icon=":material/folder:", color="orange")
        st.badge("DynamoDB", icon=":material/database:", color="blue")
        st.badge("Fargate", icon=":material/add_box:", color="violet")
        st.badge("CloudFormation", icon=":material/cloud:", color="green")
        st.badge("CloudFront", icon=":material/public:", color="blue")
        st.badge("Simple Queue Service (SQS)", icon=":material/queue:", color="green")
        st.badge("Event Bridge", icon=":material/event:", color="yellow")
    with col2:
        st.badge(
            "Elastic Container Service (ECS)", icon=":material/add_box:", color="violet"
        )
        st.badge("Lambda", icon=":material/functions:", color="yellow")
        st.badge("API Gateway", icon=":material/api:", color="green")
        st.badge("Secret Manager", icon=":material/lock:", color="red")
        st.badge("Key Management Service (KMS)", icon=":material/key:", color="red")
        st.badge("Cost Explorer", icon=":material/attach_money:", color="green")
        st.badge("CloudWatch", icon=":material/cloud_alert:", color="orange")
    with col3:
        st.badge(
            "Relational Database Service (RDS)",
            icon=":material/database:",
            color="blue",
        )
        st.badge(
            "Simple Notification Service (SNS)",
            icon=":material/notifications:",
            color="green",
        )
        st.badge("Simple Email Service (SES)", icon=":material/email:", color="blue")
        st.badge(
            "Elastic Load Balancing (ELB)", icon=":material/balance:", color="yellow"
        )
        st.badge("Parameter Store", icon=":material/settings:", color="gray")
        st.badge(
            "Identity Access Management (IAM)", icon=":material/person:", color="blue"
        )
        st.badge("EC2", icon=":material/computer:", color="yellow")
    with col4:
        st.badge("Redshift", icon=":material/analytics:", color="violet")
        st.badge(
            "Elastic Container Registry (ECR)",
            icon=":material/add_box:",
            color="violet",
        )

with Soft:
    skills = ["Communication", "Teamwork", "Time Management", "Leadership"]
    levels = [5, 4, 3, 3]

    fig = go.Figure(go.Bar(x=skills, y=levels))

    fig.update_layout(
        yaxis=dict(
            tickvals=[1, 2, 3, 4, 5],
            ticktext=["Novice", "Beginner", "Intermediate", "Advanced", "Expert"],
            range=[0, 5.5],
        )
    )

    st.plotly_chart(fig, key="soft_skills")


with Lang:
    skills = ["Python", "SQL", "C/C++", "Go", "Typescript"]
    levels = [4, 4, 1.75, 0.5, 0.5]

    fig = go.Figure(go.Bar(x=skills, y=levels, marker=dict(color="#228501")))

    fig.update_layout(
        xaxis=dict(title="Programming Languages"),
        yaxis=dict(
            title="Years Experience",
            tickvals=[1, 2, 3, 4, 5],
            range=[0, 6],
        ),
    )

    st.plotly_chart(fig, key="Languages")
with Other:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.badge("JSON", icon=":material/data_object:", color="yellow")
        st.badge("XML", icon=":material/description:", color="orange")
        st.badge("DRY Principles", icon=":material/pattern:", color="violet")
        st.badge("SOLID Principles", icon=":material/architecture:", color="blue")
        st.badge("Design Patterns", icon=":material/dashboard:", color="green")
        st.badge("Problem Solving", icon=":material/lightbulb:", color="yellow")
        st.badge("System Design", icon=":material/schema:", color="blue")
    with col2:
        st.badge("Docker", icon=":material/package:", color="blue")
        st.badge("REST APIs", icon=":material/api:", color="green")
        st.badge("Authentication", icon=":material/lock:", color="red")
        st.badge("Caching", icon=":material/bolt:", color="yellow")
        st.badge("Message Queues", icon=":material/queue:", color="violet")
        st.badge("Logging", icon=":material/description:", color="orange")
        st.badge("Monitoring", icon=":material/trending_up:", color="blue")
    with col3:
        st.badge(
            "PostgreSQL",
            icon=":material/database:",
            color="blue",
        )
        st.badge(
            "Multithreading",
            icon=":material/hourglass_empty:",
            color="orange",
        )
        st.badge("Unit Testing", icon=":material/check_circle:", color="green")
        st.badge("Code Reviews", icon=":material/rate_review:", color="yellow")
        st.badge("Git Workflows", icon=":material/merge:", color="gray")
        st.badge("Debugging", icon=":material/bug_report:", color="red")
        st.badge("Performance Tuning", icon=":material/speed:", color="green")
    with col4:
        st.badge("Linux", icon=":material/terminal:", color="grey")
        st.badge(
            "CI/CD Pipelines",
            icon=":material/integration_instructions:",
            color="violet",
        )
        st.badge("Agile Methodology", icon=":material/groups:", color="green")
        st.badge("Technical Documentation", icon=":material/article:", color="blue")
        st.badge("Mentoring", icon=":material/school:", color="orange")
        st.badge("Refactoring", icon=":material/construction:", color="yellow")
        st.badge("Scalability", icon=":material/trending_up:", color="green")
# endregion
st.divider()
# region Education
st.header("Education", text_alignment="center")
st.subheader("Wichita State University")
education, uni_logo = st.columns(2)
with education:
    st.write("""
        #### BS in Electrical Engineering | August 2023
        - Minor in Computer Science
    """)
with uni_logo:
    st.image(WSU_LOGO)

# endregion
st.divider()

# region Resume
st.header("Resume", text_alignment="center")
# Find resume in path
resume_path = None
for _, _, files in os.walk("assets"):
    for file in files:
        if "resume" in file.lower():
            resume_path = os.path.join("assets", file)
            resume_file_name = file
            break


if not resume_path:
    st.warning(
        ":construction: Oops! Looks like there was an issue looking for the resume. It must be under maintenance!"
    )
    st.stop()

filename_no_ext = file.split(".")[0]
file_date_str = filename_no_ext.split(" ")[-1]
file_date = datetime.strptime(file_date_str, "%m-%d-%Y")

st.subheader(f"Latest update: {file_date.strftime("%B %d, %Y")}")
st.pdf(f"assets/{resume_file_name}", height=830)
# 830 is just enough so that no scroll bar appears in the "iframe" (at least on my laptop...)

st.write("Want a copy?")
st.download_button(
    "Download",
    data=open(resume_path, "rb").read(),
    file_name=resume_file_name,
    mime="application/pdf",
)
# endregion
st.divider()
# region Contact
st.header("Contact", text_alignment="center")
st.write(
    "Want to get in touch? Send me an email at [isaacsaaron@gmail.com](mailto:isaacsaaron@gmail.com)! I check my inbox regularly and will get back to you as soon as I can. I also have references available upon request."
)
# endregion
