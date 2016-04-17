package me.jackfischer.jjupload;

import android.database.Cursor;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import com.thingspace.cloud.sdk.CloudAPI;

import java.util.ArrayList;


public class MainActivity extends AppCompatActivity {
    CloudAPI cloudAPI;
    String access_tok = "QKCONLMNTVLBVLCCSX2DIW2PSD7VLGIUON3CHKGWMHRNQ53JJMIQJ7SOQIBMG6UJHE4BV2PIXEYYIRWKC5PVBRGQH6LSWU7WIWCZLZN47LGOLNQ35S6TSXJODJNNHJUVQWNZVGOCCB5WBUSVSJDJXEMIGZ2UOYSEV3VGESR3S6M74F7KBCXDJD2XPZTSJM2BJS2AUQXEOP2M3ITZMCP3R4IG2GEFLRBY56N4ZSRJWMRQMXUXPBRL557SL4F2I7XJY4WOE6LGVETORVBWMC6ABUBQG2T3ZKKZOQHYR7CA3VMVCZPSUYF3EGZ4SLZ2RY6GRGI3XMG6FQFGR3JQIMDEHGUOHOCLKLTTQUVSSRA";

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
        final Button tokbutton = (Button) findViewById(R.id.tokbutton);
        tokbutton.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                gettok();
            }
        });
        String applicationID = "iz2EI43NkEq69NuqZPi1dHqm4O0a";
        String application_secret = "ybptu6xXWjwZbkxAVMcFKYL0sCIa";
        String call_back_url = "http://jackfischer.me:5000/";
        cloudAPI = new CloudAPI(applicationID, application_secret, call_back_url);
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


