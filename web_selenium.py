from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import threading

def three_thread():
    for n in range(1, 100):
        # 创建Chrome浏览器对象
        driver = webdriver.Chrome()
        time.sleep(5)
        try:
            # 清除所有cookie
            driver.delete_all_cookies()

            # 打开网页
            driver.get('https://myd.iscn.org.cn/#/s/6rPmYeqD?sourceId=632797')
            time.sleep(1)
            # 定义两个单选按钮的XPath表达式
            radio_xpaths = [
                '/html/body/div[1]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[3]/div[2]/div/form/div[2]/div/div/div/div[1]/label/span[1]/span',
                '/html/body/div[1]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[3]/div[2]/div/form/div[2]/div/div/div/div[2]/label/span[1]/span'
            ]

            # 随机选择一个单选按钮的XPath
            selected_radio_xpath = random.choice(radio_xpaths)

            # 显式等待元素加载完成并点击单选按钮
            radio_button = WebDriverWait(driver, 2).until(
                EC.element_to_be_clickable((By.XPATH, selected_radio_xpath))
            )
            radio_button.click()
            time.sleep(2)
            # 点击输入框
            input_xpath = '//*[@id="app"]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[3]/div[2]/div/form/div[3]/div/div/div/div/div/input'
            input_element = WebDriverWait(driver, 2).until(
                EC.element_to_be_clickable((By.XPATH, input_xpath))
            )
            input_element.click()

            # 定义列表项的XPath范围
            list_item_xpaths = [
                f'/html/body/div[2]/div[1]/div[1]/div[1]/ul/li[{i}]' for i in range(1, 10)
            ]
            # print(list_item_xpaths)
            # 随机选择一个列表项的XPath
            selected_list_item_xpath = random.choice(list_item_xpaths)
            # print(selected_list_item_xpath)
            # 显式等待元素加载完成并点击列表项
            list_item = WebDriverWait(driver, 2).until(
                EC.element_to_be_clickable((By.XPATH, selected_list_item_xpath))
            )
            list_item.click()
            time.sleep(2)
            # 定义第二列
            list2 = [
                f'/html/body/div[2]/div[1]/div[2]/div[1]/ul/li[{j}]' for j in range(1, 11)
            ]
            selected_list2_item_xpath = random.choice(list2)
            list2_item = WebDriverWait(driver, 2).until(
                EC.element_to_be_clickable((By.XPATH, selected_list2_item_xpath))
            )
            list2_item.click()

            time.sleep(2)
            # 教育经历
            edu = [
                f'/html/body/div[1]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[3]/div[2]/div/form/div[4]/div/div/div/div[{i}]/label/span[1]/span'
                for i in range(1, 8)
            ]
            edu_path = random.choice(edu)
            edu_item = WebDriverWait(driver,2).until(
                EC.element_to_be_clickable((By.XPATH, edu_path))
            )
            edu_item.click()
            time.sleep(2)
            # 工作
            job = [
                f'/html/body/div[1]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[3]/div[2]/div/form/div[5]/div/div/div/div[{i}]/label/span[1]/span'
                for i in range(1,7)
            ]
            job_path = random.choice(job)
            job_item = WebDriverWait(driver, 2).until(
                EC.element_to_be_clickable((By.XPATH, job_path))
            )
            job_item.click()
            time.sleep(2)
            role = [
                f'/html/body/div[1]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[3]/div[2]/div/form/div[6]/div/div/div/div[{i}]/label/span[1]/span'
                for i in range(1,9)
            ]
            role_path = random.choice(role)
            role_item = WebDriverWait(driver,2).until(
                EC.element_to_be_clickable((By.XPATH,role_path))
            )
            role_item.click()
            time.sleep(2)
            # input
            input2_xpath = '/html/body/div[1]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[3]/div[2]/div/form/div[7]/div/div/div/div[1]/div/div/input'
            input2_item = WebDriverWait(driver,2).until(
                EC.element_to_be_clickable((By.XPATH,input2_xpath))
            )
            input2_item.click()
            time.sleep(2)
            # 第一列
            first_column_options = driver.find_elements(By.XPATH, "/html/body/div[3]/div[1]/div[1]/div[1]/ul/li/span")
            # 检查第一列是否有选项
            if first_column_options:
                # 随机选择一个选项
                random_option = random.choice(first_column_options)

                # 点击随机选择的选项
                driver.execute_script("arguments[0].click();", random_option)
            time.sleep(2)

            # 第二列
            second_column_options = driver.find_elements(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[1]/ul/li/span")
            # 检查第二列是否有选项
            if second_column_options:
                print("2")
                # 随机选择一个选项
                random_option2 = random.choice(second_column_options)
                print(random_option2)
                # 点击随机选择的选项
                driver.execute_script("arguments[0].click();", random_option2)
            time.sleep(2)

            # 第三列
            third_column_options = driver.find_elements(By.XPATH, "/html/body/div[3]/div[1]/div[3]/div[1]/ul/li/span")
            # 检查第三列是否有选项
            if third_column_options:
                # 随机选择一个选项
                random_option3 = random.choice(third_column_options)

                # 点击随机选择的选项
                driver.execute_script("arguments[0].click();", random_option3)
            time.sleep(2)

            place = [
                f'/html/body/div[1]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[3]/div[2]/div/form/div[8]/div/div/div/div[{i}]/label/span[1]/span'
                for i in range(1, 3)
            ]
            place_path = random.choice(place)
            place_item = WebDriverWait(driver, 2).until(
                EC.element_to_be_clickable((By.XPATH, place_path))
            )
            place_item.click()
            time.sleep(2)

            money = driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[3]/div[2]/div/form/div[9]/div/div/div/div/label")
            # 检查 money 是否有选项
            # 随机选择一个选项
            money_option = random.choice(money)
            print(money_option)
            # 点击随机选择的选项
            driver.execute_script("arguments[0].click();", money_option)
            time.sleep(2)

            # 网龄
            web_time_input = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[3]/div[2]/div/form/div[11]/div/div/div/div/div/input")
            web_time_input.click()
            time.sleep(2)

            # 第一列
            time_column = driver.find_elements(By.XPATH, "/html/body/div[4]/div[1]/div[1]/div[1]/ul/li/span")
            # 检查第一列是否有选项
            if time_column:
                # 随机选择一个选项
                time_option = random.choice(time_column)

                # 点击随机选择的选项
                driver.execute_script("arguments[0].click();", time_option)
            time.sleep(2)

            # 第二列
            time_column2 = driver.find_elements(By.XPATH, "/html/body/div[4]/div[1]/div[2]/div[1]/ul/li/span")
            # 检查第二列是否有选项
            if time_column2:
                # 随机选择一个选项
                time_option2 = random.choice(time_column2)

                # 点击随机选择的选项
                driver.execute_script("arguments[0].click();", time_option2)
            time.sleep(2)

            time_web = driver.find_elements(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[3]/div[2]/div/form/div[12]/div/div/div/div/label/span[1]/span")
            time_web_option = random.choice(time_web)
            driver.execute_script("arguments[0].click();", time_web_option)
            time.sleep(2)

            # spend money
            spendmoney = driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[3]/div[2]/div/form/div[13]/div/div/div/div/label/span[1]")
            # 检查 spend money 是否有选项
            # 随机选择一个选项
            spend_money_option = random.choice(spendmoney)
            # 点击随机选择的选项
            driver.execute_script("arguments[0].click();", spend_money_option)
            time.sleep(2)

            # cheap or expensive
            ce =  driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[3]/div[2]/div/form/div[14]/div/div/div/div[1]/label/span[1]/span")
            ce_option = random.choice(ce)
            driver.execute_script("arguments[0].click()",ce_option)
            time.sleep(2)

            for i in range(15, 19):
                all = driver.find_elements(By.XPATH,f"/html/body/div[1]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[3]/div[2]/div/form/div[{i}]/div/div/div/div/div[1]/label/span[1]/span")
                option = random.choice(all)
                driver.execute_script("arguments[0].click()",option)
            time.sleep(2)

            for i in range(1, 6):
                click = driver.find_element(By.XPATH,f"/html/body/div[1]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[3]/div[2]/div/form/div[19]/div/div/div[1]/div/div[2]/div[{i}]/div[2]/span[10]/i")
                driver.execute_script("arguments[0].click()",click)
            time.sleep(2)

            for i in range(20, 22):
                click = driver.find_element(By.XPATH,f"/html/body/div[1]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[3]/div[2]/div/form/div[{i}]/div/div/div/div[1]/label/span[1]/span")
                driver.execute_script("arguments[0].click()", click)
            time.sleep(2)

            for i in range(1, 8):
                click = driver.find_element(By.XPATH,f"/html/body/div[1]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[3]/div[2]/div/form/div[22]/div/div/div/div/div[2]/div[{i}]/div[2]/span[10]/i")
                driver.execute_script("arguments[0].click()", click)
            time.sleep(2)

            # 等待元素加载
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[3]/div[2]/div/form/div[23]/div/div/div/div/button/span'))
            )

            # 点击元素
            element.click()

            time.sleep(20)

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            # 关闭浏览器
            driver.quit()


thread1 = threading.Thread(target=three_thread)
thread2 = threading.Thread(target=three_thread)
thread3 = threading.Thread(target=three_thread)
thread4 = threading.Thread(target=three_thread)
thread5 = threading.Thread(target=three_thread)
# 启动线程
thread1.start()
time.sleep(1)
thread2.start()
time.sleep(1)
thread3.start()
time.sleep(1)
thread4.start()
time.sleep(1)
thread5.start()
# 等待线程完成
thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()