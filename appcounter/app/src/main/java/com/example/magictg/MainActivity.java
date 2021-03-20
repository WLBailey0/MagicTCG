package com.example.magictg;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
int playerHealth = 20;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        TextView healthTextView = (TextView) findViewById(R.id.healthTextView);
        Button lifeUpButton = (Button) findViewById(R.id.lifeUpButton);
        Button lifeDownButton = (Button)findViewById(R.id.lifeDownButton);

        lifeUpButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                playerHealth++;
                healthTextView.setText("" + playerHealth);
                
            }
        });
        lifeDownButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                playerHealth--;
                healthTextView.setText("" + playerHealth);

            }
        });
    }
}