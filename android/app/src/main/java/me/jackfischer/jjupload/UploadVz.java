package me.jackfischer.jjupload;

import android.content.Context;
import android.os.AsyncTask;

import com.thingspace.cloud.sdk.CloudAPI;

/**
 * Created by jack on 4/17/16.
 */
public class UploadVz extends AsyncTask<Integer, Void, Void> {
    private Context mContext;
    private CloudAPI mcloudAPI;
    public UploadVz(Context context, CloudAPI cloudAPI){
        mContext = context;
        mcloudAPI = cloudAPI;
    }

     protected Void doInBackground(Integer... inp)  {
         String filename = "jjfile.txt";
         //String path = mContext.getFilesDir().toString() + "/" + filename;
         String path = mContext.getFilesDir().toString();
         System.out.println(path);
         mcloudAPI.uploadFile(mContext, "VZMOBILE/jj/", filename, path);
         System.out.println("FINISHED UPLOAD!!!!!!!!!!!");
         return null;
     }

    protected void onPostExecute() {
        // TODO: check this.exception
        // TODO: do something with the feed
    }
}
