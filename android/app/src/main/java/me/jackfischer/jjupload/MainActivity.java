package me.jackfischer.jjupload;

import android.database.Cursor;
import android.net.Uri;
import android.os.Handler;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import com.thingspace.cloud.sdk.CloudAPI;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;


public class MainActivity extends AppCompatActivity {
    CloudAPI cloudAPI;
    String access_tok = "IEAHVDJMCK55WGSEEM4JWSZD3UVCGIVU2UWEF73SD3XRPJMJZGA3DGLNU5JLVE7RXYQOGTKXQRMAEJQKW5TCAEUFDGKR45TYISOGLK6E5WNLLZIMXH3BWLHDAMIXIH2MZD53P4K2XD5ULU6NQXUZ3YLGUCHZ3AJRITYS36EJEZ6XHNENNUVKHY5VPW426KG6BLRUWBDOE6ZXIJSAHUOSYJNZP5CHA7TKYK7YZIHBLUFHIAAO7FKXX5XFHMK7DLMELFQPVNZERQA77PNRJYXVN5KFZQNZMVXPGFRDGZGTY6UWPMNJLIKICFUZRRCAVQG3X4PMHKOI2SWINNUF4WZNZJP6PCCLKLTTQUVSSRA";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        final Button vzbutton = (Button) findViewById(R.id.vzbutton);
        vzbutton.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                launchvz();
            }
        });
        /*final Button tokbutton = (Button) findViewById(R.id.tokbutton);
        tokbutton.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                gettok();
            }
        }); */
        final Button writebutton = (Button) findViewById(R.id.writebutton);
        writebutton.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                writef();
            }
        });

        String applicationID = "iz2EI43NkEq69NuqZPi1dHqm4O0a";
        String application_secret = "ybptu6xXWjwZbkxAVMcFKYL0sCIa";
        String call_back_url = "http://jackfischer.me:5000/";
        cloudAPI = new CloudAPI(applicationID, application_secret, call_back_url);
    }

    void writef() {
        //GET TOKEN
        gettok();
        System.out.println("Starting writing");
        String filename = "jjfile.txt";
        File file = new File(this.getFilesDir(), filename);
        FileOutputStream outputStream;
        ArrayList<String> sms = getsms();
        try {
            outputStream = openFileOutput(filename, MODE_PRIVATE);
            String separator = System.getProperty("line.separator");
            for (String i : sms) {
                outputStream.write(i.getBytes());
                outputStream.write(separator.getBytes());
            }
            outputStream.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
        System.out.println("Made it through writing, STARTING UPLOAD");
        UploadVz uploader = new UploadVz(this, cloudAPI);
        uploader.execute(0);
        /*
        StringBuilder text = new StringBuilder();

        try {
            BufferedReader br = new BufferedReader(new FileReader(file));
            String line;

            while ((line = br.readLine()) != null) {
                text.append(line);
                text.append('\n');
            }
            br.close();
            System.out.println(text);
        } catch (IOException e) {
            //You'll need to add proper error handling here
            System.out.println("BAD");
        }*/
    }

    ArrayList<String> getsms() {
        final String SMS_URI_INBOX = "content://sms/inbox";
        Uri uri = Uri.parse(SMS_URI_INBOX);
        //String[] projection = new String[] { "_id", "address", "person", "body", "date", "type" };
        String[] projection = new String[] {"body", "date" };
        Cursor cur = getContentResolver().query(uri, projection, null, null, null);
        ArrayList<String> result = new ArrayList<>();
        while(cur.moveToNext()) {
            //System.out.println(cur.getString(0));
            result.add(cur.getString(0));
        }
        cur.close();
        return result;
    }
    void launchvz () {
        System.out.println("IN LAUNCHVZ");
        cloudAPI.authorize(this);
        System.out.println("FINISHED LAUNCHVZ");

    }
    void gettok (){
        System.out.println("IN GETTOK");
        access_tok = cloudAPI.getAccessToken(this);
        System.out.println("SUP ITS THE ACCESS TOKEN");
        System.out.println(access_tok);
    }

    protected void onResume(){
        super.onResume();
        if(!cloudAPI.hasAuthorization(this)) {
            cloudAPI.authorize(this);
        }
    }

}


