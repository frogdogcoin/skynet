package com.frogdog.skynet;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.time.Duration;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Set;
import java.util.Vector;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.firefox.FirefoxOptions;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;


public class RunTwitterUserLoginTweetPepeMP4 {
    private static final String DIRECTORY_PATH = "C:\\wd\\py\\vid.pepe\\";
    private static final String[] VIDEO_EXTENSIONS = new String[] {".mp4", ".avi", ".flv", ".wmv", ".mov", ".mkv"};

    private static Random rand = new Random();
	public RunTwitterUserLoginTweetPepeMP4() {
		// TODO Auto-generated constructor stub
	}
	public static void main(String[] args) {
		
		String glbUrl =  "https://twitter.com";
		String searchinput = " ";
		int minRange = 0;
        int maxRange = 16; // the maximum value of the range
        int loops = 5;
         String websiteurl = " #ribbit";
         Random random = new Random(); 
            
        String chat = "create a tweet hybrid is the new meta frogdog is the king of hybrid frog and dog is the ultimate hyrbrid write in style of hunter s thompson  ";
 
		              
        
        for(int c=0;c<10;c++) {
        chat = chat.replace(" ", "_");  
        	TwitterUsers users = new TwitterUsers();
            for (String[] credentials : users.getUserCredentials()) {
                        String username = credentials[0];
                        String password = credentials[1];
						try {
							
		
							
							
				        System.setProperty("webdriver.chrome.driver", "C:\\wd\\chromedriver.exe");		        
				        ChromeOptions options = new ChromeOptions();
				        options.addArguments("--no-sandbox");		        
				        options.setBinary("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe");
				        WebDriver driver = new ChromeDriver();
						driver.manage().deleteAllCookies();
						driver.manage().timeouts().pageLoadTimeout(40, TimeUnit.SECONDS);
			        	
						driver.get(glbUrl); 
						driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
			        Vector<String> animalVec = new Vector<String>();
					 try {								
										Thread.sleep(1000); 
										System.out.println(glbUrl); 
										WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
										wait.until(ExpectedConditions.presenceOfElementLocated(By.cssSelector("body")));								
										WebElement loginElement = driver.findElement(By.xpath("//span[contains(text(), 'Sign in')]"));
										loginElement.click();	
								        
								        // Introduce random delay between actions (e.g., 2 to 5 seconds)
								        int delay = 2000 + new Random().nextInt(3000);
								        Thread.sleep(delay);
		
								        WebElement textInput = driver.findElement(By.cssSelector("input[name='text'][type='text']"));
								        textInput.sendKeys(username);	
								        
								        WebElement nextElement = driver.findElement(By.xpath("//span[contains(text(), 'Next')]"));
								        nextElement.click();					        
		
								        WebElement textInputp = driver.findElement(By.cssSelector("input[name='password'][type='password']"));
								        textInputp.sendKeys(password);	
		 				        
								        for (int i = 0; i < 3; i++) {
								            driver.switchTo().activeElement().sendKeys(Keys.TAB);
								        }
		
								        // Simulate pressing Enter key on the active element
								        driver.switchTo().activeElement().sendKeys(Keys.ENTER);
								        
								        
							            WebElement tweetButton = driver.findElement(By.cssSelector("a[data-testid='SideNav_NewTweet_Button']"));
							            tweetButton.click();

							            // Wait until the tweet box is shown
							            Thread.sleep(2000);

							            
							            List<File> videoFiles = getVideoFiles(new File(DIRECTORY_PATH));
							             
							            if (!videoFiles.isEmpty()) {
							                File randomVideoFile = videoFiles.get(random.nextInt(videoFiles.size()));
							                System.out.println("Random video file: " + randomVideoFile.getAbsolutePath());
								            WebElement fileInput = driver.findElement(By.cssSelector("input[type='file']"));
								            fileInput.sendKeys(randomVideoFile.getAbsolutePath());	
							            } else {
							                System.out.println("No video files found in the directory: " + DIRECTORY_PATH);
							            }

							            Thread.sleep(179000);
							           
							            // Enter your tweet
							            String tweet = new String(); 
							            
							            if(true) {
							            String command = "python C:\\wd\\py\\openaitweet.py " + chat;
							            
							            // Create the process builder
							            ProcessBuilder pb = new ProcessBuilder(command.split(" "));
							            pb.redirectErrorStream(true);
							            
							            // Start the process
							            Process process = pb.start();
							            
							            // Read the output from the Python script
							            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
							            String line;
							            while ((line = reader.readLine()) != null) {
							            	tweet +=line;
							            }
							            // Wait for the process to finish
							            if(tweet.length()>240) { 
									        driver.quit();
							            	continue;
							            }
							            int exitCode = process.waitFor();
							            System.out.println("Python script exited with code: " + exitCode);

							            }
							            
							            // Find the tweet box
							            WebElement tweetBox = driver.findElement(By.xpath("//div[@aria-label='Tweet text']"));

							            tweet += " " + websiteurl ;
							            tweetBox.sendKeys(tweet + " ");

							            // Wait a bit for tweet to be ready to send
							            Thread.sleep(2000);
							            
							             
							            WebElement replyElement = driver.findElement(By.xpath("//*[contains(text(),'Tweet')]"));

							            // Use JavaScript to set the focus to the reply element
							            JavascriptExecutor jsExecutor = (JavascriptExecutor) driver;
							            jsExecutor.executeScript("arguments[0].focus();", replyElement);
							            jsExecutor.executeScript("arguments[0].click();", replyElement);
							            System.out.println("---------------------------------------------------------------------------");
							            Thread.sleep(21100);
		
								        // Simulate pressing Enter key on the active element
//								        driver.switchTo().activeElement().sendKeys(Keys.ENTER);							        
								        
								        driver.quit();
										//driver.get(glbUrlSpace); 
										//driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
										//wait.until(ExpectedConditions.presenceOfElementLocated(By.cssSelector("body")));
										
										//WebElement listenLiveElement = driver.findElement(By.xpath("//span[contains(text(), 'Listen live')]"));
								        //listenLiveElement.click();
		
										//wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath("//span[contains(text(), 'Join this Space')]")));
										
										//WebElement joinLiveElement = driver.findElement(By.xpath("//span[contains(text(), 'Join this Space')]"));
										//joinLiveElement.click();
								        
					} catch (Exception ex) {
					    ex.printStackTrace();
					}
						}catch(Exception ex) {
							ex.printStackTrace();
						}
		
					}
		            try {
		            	 int delayInSeconds = new Random().nextInt(35) + 10;
		                Thread.sleep(delayInSeconds * 1000);
		            } catch (InterruptedException e) {
		                e.printStackTrace();
		            }
		            
        }     
		          
	}
	
    private static int getRandomNumberInRange(int min, int max) {
        if (min >= max) {
            throw new IllegalArgumentException("Max must be greater than min");
        }
        
        return rand.nextInt((max - min) + 1) + min;
    }
    private static List<File> getVideoFiles(File folder) {
        List<File> videoFiles = new ArrayList<File>();
        File[] files = folder.listFiles();

        if (files != null) {
            for (File file : files) {
                if (file.isFile() && isVideoFile(file)) {
                    videoFiles.add(file);
                }
            }
        }
        return videoFiles;
    }

    private static boolean isVideoFile(File file) {
        String name = file.getName();
        for (String extension : VIDEO_EXTENSIONS) {
            if (name.toLowerCase().endsWith(extension)) {
                return true;
            }
        }
        return false;
    }
    
}
