from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import re


def get_course_links():
    driver = webdriver.Chrome()
    driver.get("https://mate.academy")
    time.sleep(5)

    courses = driver.find_elements(By.CLASS_NAME, "ProfessionCard_title__m7uno")
    links = [course.find_element(By.XPATH, "./ancestor::a").get_attribute("href") for course in courses]
    driver.quit()
    return links


def scrape_course_details(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)

    course_name = driver.find_element(By.CLASS_NAME, "CoursesHeadingText_heading__4tGVX").text

    try:
        course_description = driver.find_element(By.CLASS_NAME, "SalarySection_aboutProfession__C6ftM").text
    except:
        course_description = "N/A"

    durations = driver.find_elements(By.CLASS_NAME, "TableFeedView_rowContent__Nih2n")
    full_time_duration = "N/A"
    flex_time_duration = "N/A"

    if len(durations) >= 2:
        full_time_duration = durations[6].text.strip()
        flex_time_duration = durations[17].text.strip()

    modules = driver.find_elements(By.CLASS_NAME, "CourseModulesList_topicName__7vxtk")
    topics = driver.find_elements(By.CLASS_NAME, "CourseModulesList_topicsCount__H_fv3")

    data_topic = [el.text for el in topics]

    num_modules = len(modules)
    num_topics = 0

    for el in data_topic:
        for str_ in el.split():
            if str_.isdigit():
                num_topics += int(str_)

    driver.quit()

    course_data = []

    if full_time_duration != "N/A":
        course_data.append([course_name, course_description, "Full-Time", full_time_duration, num_modules, num_topics])

    if flex_time_duration != "N/A":
        course_data.append([course_name, course_description, "Flex", flex_time_duration, num_modules, num_topics])

    return course_data


def main():
    course_links = get_course_links()

    with open("mate_academy_courses.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Course Name", "Description", "Course Type", "Duration", "Modules", "Topics"])

        for link in course_links:
            data = scrape_course_details(link)
            for row in data:
                writer.writerow(row)

    print("Scraping completed and saved to mate_academy_courses.csv")


if __name__ == "__main__":
    main()
