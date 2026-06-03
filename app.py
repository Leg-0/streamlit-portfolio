import streamlit as st
import os
from datetime import datetime
from pathlib import Path
import plotly.graph_objects as go

st.set_page_config(
    initial_sidebar_state="expanded",
    layout="wide",
    page_title="Aaron Isaacs Portfolio",
    page_icon=":octopus:",
)
PHOTO_OF_ME = "assets/headshot_transparent.png"
WSU_LOGO = "assets/Wichita_State_University_logo.png"
SNOWFLAKE_LOGO = "assets/snowflake.png"


def experience_header(company, dates):
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(company, divider=True, text_alignment="left")
    with col2:
        st.subheader(dates, divider=True, text_alignment="right")


@st.cache_data
def load_resume_bytes(path):
    return Path(path).read_bytes()


@st.cache_data
def build_soft_skills_fig():
    fig = go.Figure(
        go.Bar(
            x=["Communication", "Teamwork", "Time Management", "Leadership"],
            y=[5, 4, 3, 3],
        )
    )
    fig.update_layout(
        yaxis=dict(
            tickvals=[1, 2, 3, 4, 5],
            ticktext=["Novice", "Beginner", "Intermediate", "Advanced", "Expert"],
            range=[0, 5.5],
        )
    )
    return fig


@st.cache_data
def build_coding_languages_fig():
    fig = go.Figure(
        go.Bar(
            x=["Python", "SQL", "C/C++", "Go", "Typescript", "PowerShell"],
            y=[4, 4, 1.75, 0.5, 0.5, 0.75],
            marker=dict(color="#0066cc"),
        )
    )
    fig.update_layout(
        xaxis=dict(title="Programming Languages"),
        yaxis=dict(
            title="Years Experience",
            tickvals=[1, 2, 3, 4, 5],
            range=[0, 6],
        ),
    )
    return fig


@st.cache_data
def build_spoken_languages_fig():
    fig = go.Figure(
        go.Bar(
            x=["Italian", "German", "English"],
            y=[2, 1, 6],
            marker=dict(color="#008C45"),
        )
    )
    fig.update_layout(
        xaxis=dict(title="Spoken Languages"),
        yaxis=dict(
            title="CEFR Level",
            tickvals=[1, 2, 3, 4, 5, 6],
            ticktext=["A1", "A2", "B1", "B2", "C1", "C2"],
            range=[0, 6],
        ),
    )
    return fig

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
    experience_header("Koch Capabilities, LLC", "Jan 2024 - Present")
    TPL, SWE = st.columns(2)
    with TPL:
        st.write("#### Technical Product Lead")
        st.write("""
            - Collaborating closely with data product owners (DPOs), technical product owners (TPOs), and stakeholders to guide technology decisions, actively solving problems with technologies that benefit stakeholders and prevent major disruptions to the tech stack.
            - Acting as the subject matter expert for our internal Streamlit web application, fielding technical questions on connectivity, scalability, ease of transformation, and compatibility.
            - Delegating product enhancements to engineers while maintaining an active hand in development, ensuring the team has the resources and support needed to be successful.
            - Planned, led, and executed a cross-stack spike between the Technology and Security organizations to establish shared access management mechanisms that both teams could understand and manage easily.
            - Empowered the team with agentic coding technology, hosting knowledge transfers about claude code and open code as well as how to build skills, agents, hooks, plugins, and more.
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
            - Created AI skill, prompt, and instruction files to support consistent automation, improve prompt engineering practices, and document reusable workflows for team-wide use.
            """)

with PE:
    experience_header("Koch Ag. & Energy Solutions, LLC", "July 2023 - Jan 2024")
    st.subheader(
        "Platform Engineer",
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
    experience_header("Georgia-Pacific, LLC", "Jan 2023 - May 2023")
    st.subheader(
        "Data Engineer Co-op",
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
General, AWS, Soft, Lang = st.tabs(["General", "AWS", "Soft", "Languages"])

with General:
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.badge("JSON", icon=":material/data_object:", color="blue")
        st.badge("XML", icon=":material/code:", color="orange")
        st.badge("DRY Principles", icon=":material/dry_cleaning:", color="violet")
        st.badge("SOLID Principles", icon=":material/architecture:", color="blue")
        st.badge("Problem Solving", icon=":material/psychology:", color="yellow")
        st.badge("System Design", icon=":material/schema:", color="violet")
        st.badge("Code Reviews", icon=":material/compare:", color="green")

    with col2:
        st.badge("Snowflake", icon=":material/ac_unit:", color="blue")
        st.badge("dbt", icon=":material/developer_mode:", color="green")
        st.badge("Redis", icon=":material/storage:", color="red")
        st.badge("Caching", icon=":material/bolt:", color="yellow")
        st.badge("Message Queues", icon=":material/queue:", color="violet")
        st.badge("Logging", icon=":material/receipt_long:", color="orange")
        st.badge("Monitoring", icon=":material/monitor_heart:", color="green")
    with col3:
        st.badge(
            "NoSQL",
            icon=":material/storage:",
            color="blue",
        )
        st.badge(
            "Multithreading",
            icon=":material/airwave:",
            color="orange",
        )
        st.badge("Unit Testing", icon=":material/check_circle:", color="green")
        st.badge(
            "Test Driven Dev (TDD)",
            icon=":material/science:",
            color="yellow",
        )
        st.badge("Git Workflows", icon=":material/merge:", color="gray")
        st.badge("Debugging", icon=":material/bug_report:", color="red")
        st.badge("Performance Tuning", icon=":material/speed:", color="green")
    with col4:
        st.badge(
            "Object Oriented Programming",
            icon=":material/code:",
            color="gray",
        )
        st.badge(
            "CI/CD Pipelines",
            icon=":material/integration_instructions:",
            color="violet",
        )
        st.badge("Agile Methodology", icon=":material/groups:", color="green")
        st.badge("Technical Documentation", icon=":material/article:", color="blue")
        st.badge("Authentication", icon=":material/security:", color="orange")
        st.badge("Refactoring", icon=":material/build:", color="yellow")
        st.badge("Scalability", icon=":material/trending_up:", color="green")
    with col5:
        st.badge("PDM", icon=":material/package_2:", color="gray")
        st.badge(
            "uv",
            icon=":material/visibility:",
            color="violet",
        )
        st.badge("Pandas", icon=":material/table_chart:", color="green")
        st.badge("FastAPI", icon=":material/api:", color="blue")
        st.badge("REST APIs", icon=":material/api:", color="orange")
        st.badge("dlt", icon=":material/download:", color="yellow")
        st.badge("Docker", icon=":material/layers:", color="blue")

    with col6:
        st.badge("Streamlit", icon=":material/monitor:", color="grey")
        st.badge(
            "Linux",
            icon=":material/terminal:",
            color="violet",
        )
        st.badge("boto3", icon=":material/cloud:", color="green")
        st.badge("pydantic", icon=":material/shield:", color="blue")
        st.badge("pytest", icon=":material/auto_fix_high:", color="orange")
        st.badge("asyncio", icon=":material/sync_alt:", color="yellow")
        st.badge("requests/httpx", icon=":material/send:", color="green")

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
        st.badge("Bedrock", icon=":material/robot:", color="gray")

with Soft:
    st.plotly_chart(build_soft_skills_fig(), key="soft_skills")

with Lang:
    col_coding, col_spoken = st.columns([3, 1])

    with col_coding:
        st.plotly_chart(build_coding_languages_fig(), key="CodingLanguages")

    with col_spoken:
        st.plotly_chart(build_spoken_languages_fig(), key="SpokenLanguages")
# endregion
st.divider()
# region Education
st.header("Education", text_alignment="center")
st.subheader("Wichita State University")
education, uni_logo = st.columns(2)
with education:
    st.write("""
        #### BS in Electrical Engineering | June 2023
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
resume_file_name = None
for _, _, files in os.walk("assets"):
    for file in files:
        if "resume" in file.lower():
            resume_file_name = file
            resume_path = os.path.join("assets", file)
            break
    if resume_path:
        break


if not resume_path:
    st.warning(
        ":construction: Oops! Looks like there was an issue looking for the resume. It must be under maintenance!"
    )
    st.stop()

# Prefer the date embedded in the filename (e.g. "... 5-28-2026.pdf") since it
# reflects when the resume was actually updated. Fall back to the file's
# modification time if the name doesn't contain a parseable date.
date_token = Path(resume_file_name).stem.split(" ")[-1]
try:
    file_date = datetime.strptime(date_token, "%m-%d-%Y")
except ValueError:
    file_date = datetime.fromtimestamp(os.path.getmtime(resume_path))

st.subheader(f"Latest update: {file_date.strftime('%B %d, %Y')}")
st.pdf(resume_path, height=830)
# 830 is just enough so that no scroll bar appears in the "iframe" (at least on my laptop...)

st.write("Want a copy?")
st.download_button(
    "Download",
    data=load_resume_bytes(resume_path),
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
st.link_button(
    "LinkedIn",
    "https://www.linkedin.com/in/aaron-m-isaacs/",
    icon=":material/work:",
)
st.link_button(
    "GitHub",
    "https://github.com/Leg-0",
    icon=":material/code:",
)
# endregion
