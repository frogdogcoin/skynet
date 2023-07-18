package com.frogdog.skynet;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class TwitterUsers {
	public static String users[] = new String[]{};
	public static String usersp[] = new String[]{};

    private String[][] userCredentials;
	public String[][] getUserCredentials() {
		return userCredentials;
	}

	public void setUserCredentials(String[][] userCredentials) {
		this.userCredentials = userCredentials;
	}

	public TwitterUsers() {
		// TODO Auto-generated constructor stub
		for(int j=0;j<users.length;j++) {
			System.out.println(users[j] + "," + usersp[j]);
		}
        String filePath = "C:\\wd\\py\\users.txt";

        try {
        	BufferedReader br = new BufferedReader(new FileReader(filePath));
            String line;
            int numLines = 0;

            // Count the number of lines in the file
            while ((line = br.readLine()) != null) {
                numLines++;
            }

            // Reset the BufferedReader
            br.close();
            br = new BufferedReader(new FileReader(filePath));

            // Initialize the array with the correct size
            userCredentials = new String[numLines][];

            // Read the file again and populate the array
            int i = 0;
            while ((line = br.readLine()) != null) {
                String[] credentials = line.split(",");
                userCredentials[i] = credentials;
                i++;
            }

            // Print the usernames and passwords
            for (String[] credentials : userCredentials) {
                String username = credentials[0];
                String password = credentials[1];
                System.out.println("Username: " + username + ", Password: " + password);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }		
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
