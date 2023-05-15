// import java.io.*;
// import java.net.*;

// public class ChatClient {
//     public static void main(String[] args) {
//         try {
//             Socket socket = new Socket("localhost", 8000); // Connect to server
//             BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream())); // Input stream from server
//             PrintWriter out = new PrintWriter(socket.getOutputStream(), true); // Output stream to server
            
//             BufferedReader userInput = new BufferedReader(new InputStreamReader(System.in)); // User input stream
            
//             String input;
//             while ((input = userInput.readLine()) != null) { // Read user input
//                 out.println(input); // Send user input to server
//                 System.out.println(in.readLine()); // Print server response
//             }
            
//             socket.close(); // Close connection
//         } catch (IOException e) {
//             e.printStackTrace();
//         }
//     }
// }

import java.io.*;
import java.net.*;

public class ChatServer {
    public static void main(String[] args) {
        try {
            ServerSocket serverSocket = new ServerSocket(8000); // Start server on port 8000
            Socket clientSocket = serverSocket.accept(); // Accept incoming client connections
            
            BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream())); // Input stream from client
            PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true); // Output stream to client
            
            String input;
            while ((input = in.readLine()) != null) { // Read client input
                out.println("Server: " + input); // Send response to client
            }
            
            clientSocket.close(); // Close client connection
            serverSocket.close(); // Close server
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
