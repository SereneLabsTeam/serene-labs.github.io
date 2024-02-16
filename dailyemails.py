import json
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email_responses_url = 'https://api.sheety.co/6effe30463f484117c5d9e81cba70038/emails(sereneLabs)/formResponses1'
form_responses_url = 'https://api.sheety.co/6effe30463f484117c5d9e81cba70038/quiz(sereneLabs)/formResponses1'
token = '.QUX4-5z8HwcH#*2TF5_'

headers = {
    'Authorization': f'Bearer {token}',
}
headaches = {
    1: {
        'activity': 'Scalp Massage',
        'instructions': 'Find a comfortable sitting or lying position. Use your fingertips to gently massage your scalp in circular motions. Start at the base of your skull and work your way up to the crown of your head. Pay special attention to areas where tension tends to accumulate.',
        'benefits': 'This scalp massage stimulates blood flow to the scalp, promoting relaxation and alleviating tension headaches. The gentle circular motions help release muscle tightness and contribute to an overall sense of well-being.'
    },
    2: {
        'activity': 'Eye Exercises',
        'instructions': 'Sit or stand comfortably. Look up and down, then move your eyes from side to side without moving your head. Rotate your eyes in a circular motion. Focus on an object in the distance for a few seconds, then shift your focus to something up close.',
        'benefits': 'These eye exercises help ease eye strain and tension, common contributors to headaches. The varied movements also promote flexibility and reduce the risk of discomfort caused by prolonged screen time or other visually demanding activities.'
    },
    3: {
        'activity': 'Maintain a Regular Sleep Schedule',
        'tip': 'Establish a consistent sleep routine. Go to bed and wake up at the same time each day. Create a calming pre-sleep routine to signal to your body that it\'s time to wind down.',
        'benefits': 'Adequate and consistent sleep supports overall well-being. It plays a crucial role in managing pain and promoting a healthy immune system. A regular sleep schedule helps regulate your body\'s internal clock, optimizing the quality of your sleep.'
    },
    4: {
        'activity': 'Neck Rotation and Tilt',
        'instructions': 'Sit or stand with a straight spine. Slowly turn your head to one side, bringing your chin towards your shoulder. Hold for 15-30 seconds. Tilt your head to one side, bringing your ear towards your shoulder. Hold for 15-30 seconds. Repeat on the other side.',
        'benefits': 'This exercise promotes flexibility and releases tension in the neck and upper shoulders. It\'s particularly effective in reducing stiffness and discomfort caused by prolonged periods of sitting or staring at screens.'
    },
    5: {
        'activity': 'Hot and Cold Therapy',
        'instructions': 'Apply a hot or cold pack to the forehead or neck. Use a cloth to protect your skin from direct contact. Apply for 15 minutes, then take a break before reapplying if needed.',
        'benefits': 'Hot and cold therapy provides comfort and helps reduce inflammation. Cold packs can constrict blood vessels, reducing pain, while heat packs relax muscles and improve blood circulation. Use the temperature that feels most soothing for your specific headache type.'
    },
    6: {
        'activity': 'Forehead Massage',
        'instructions': 'Sit comfortably and use your thumbs to gently massage your forehead in circular motions. Apply pressure to the temples and the bridge of the nose.',
        'benefits': 'This massage technique relaxes the muscles and blood vessels in the forehead, reducing headache pain and inflammation. The gentle pressure on the temples can also help alleviate tension in the surrounding areas.'
    },
    7: {
        'activity': 'Neck Stretches',
        'instructions': 'Sit or stand with a straight spine. Slowly tilt your head to one side, bringing your ear towards your shoulder. Hold for 15-30 seconds and repeat on the other side. Perform gentle neck rotations as well.',
        'benefits': 'These stretches relieve tension in the neck muscles, reducing headache symptoms. The gentle rotations and tilts improve flexibility and alleviate stiffness in the neck and upper shoulders.'
    },
    8: {
        'activity': 'Social Connection',
        'tip': 'Set aside time to connect with friends or family, either in person or virtually. Share your experiences and feelings with a supportive network.',
        'benefits': 'Social support positively impacts mental and emotional well-being, influencing how pain is perceived. Connecting with others fosters a sense of belonging and can provide a distraction from chronic pain, contributing to an improved mood.'
    },
    9: {
        'activity': 'Mind-Body Practices',
        'tip': 'Explore mind-body practices like yoga or tai chi. Start with beginner-friendly poses or movements.',
        'benefits': 'Mind-body practices combine gentle movement with mindfulness, promoting relaxation and flexibility. These activities can help reduce muscle tension, enhance body awareness, and contribute to an overall sense of well-being.'
    },
    10: {
        'activity': 'Pacing Activities',
        'tip': 'Break tasks into smaller, manageable segments. Take breaks as needed to prevent overexertion.',
        'benefits': 'Pacing activities helps avoid overexertion and minimizes the risk of pain flare-ups. It allows you to manage your energy levels more effectively and maintain a consistent level of productivity without causing strain or exacerbating existing pain.'
    },
    11: {
        'activity': 'Deep Breathing',
        'instructions': 'Find a quiet place to sit comfortably. Inhale through your nose for a count of four, hold for four counts, and exhale through your mouth for a count of four. Repeat for 5-10 minutes.',
        'benefits': 'Deep breathing promotes relaxation and reduces stress, addressing potential headache triggers. It activates the body\'s relaxation response, leading to a sense of calm and improved overall well-being.'
    },
    12: {
        'activity': 'Healthy Diet',
        'tip': 'Maintain a balanced diet with a focus on whole foods. Avoid foods that may trigger inflammation or exacerbate pain, such as processed foods or those high in sugar.',
        'benefits': 'A healthy diet supports overall health and helps manage potential pain triggers. Nutrient-rich foods provide essential vitamins and minerals that contribute to overall well-being and can positively impact inflammatory processes in the body.'
    },
    13: {
        'activity': 'Stress Management',
        'tip': 'Practice stress-reducing techniques such as mindfulness, meditation, or deep breathing exercises. Incorporate stress-relief activities into your daily routine.',
        'benefits': 'Stress is a significant contributor to chronic pain. Managing stress through mindfulness and relaxation techniques can positively impact physical and mental well-being, reducing the likelihood of headaches and other pain symptoms.'
    },
    14: {
        'activity': 'Head and Neck Massage',
        'instructions': 'Gently massage your head, neck, and shoulders using circular motions and kneading techniques. Apply gentle pressure based on your comfort level.',
        'benefits': 'This massage technique relaxes tense muscles and promotes blood circulation. It provides relief from headaches by reducing muscle tension in the head and neck area, contributing to an overall sense of relaxation.'
    },
    15: {
        'activity': 'Aromatherapy',
        'instructions': 'Use calming essential oils like lavender or peppermint. Inhale the scent deeply during stressful moments. Consider using an essential oil diffuser or applying diluted oil to pulse points.',
        'benefits': 'Aromatherapy may help reduce stress and promote relaxation, contributing to headache relief. The soothing scents of essential oils can have a positive impact on mood and create a calming atmosphere.'
    },
    16: {
        'activity': 'Maintain a Regular Sleep Schedule',
        'tip': 'Stick to a consistent sleep routine. Create a calming bedtime ritual to signal to your body that it\'s time to wind down.',
        'benefits': 'Adequate and consistent sleep supports overall well-being. A regular sleep schedule helps regulate your body\'s internal clock, optimizing the quality of your sleep and contributing to pain management.'
    },
    17: {
        'activity': 'Mindful Breathing Techniques',
        'instructions': 'Practice mindfulness-based breathing exercises. Focus on deep and intentional breaths. Inhale slowly through your nose, hold for a moment, and exhale gradually through your mouth.',
        'benefits': 'Mindful breathing techniques calm the nervous system, reduce stress, and help manage headache triggers. It brings awareness to the present moment, fostering a sense of peace and relaxation.'
    },
    18: {
        'activity': 'Neck Rotation and Tilt',
        'instructions': 'Sit or stand with a straight spine. Slowly turn your head to one side, bringing your chin towards your shoulder. Hold for 15-30 seconds. Tilt your head to one side, bringing your ear towards your shoulder. Hold for 15-30 seconds. Repeat on the other side.',
        'benefits': 'This exercise promotes flexibility and releases tension in the neck and upper shoulders. It\'s particularly effective in reducing stiffness and discomfort caused by prolonged periods of sitting or staring at screens.'
    },
    19: {
        'activity': 'Pain Diary',
        'tip': 'Keep a pain diary to track activities, symptoms, and potential triggers. Note the intensity and duration of pain, as well as any factors that may influence it.',
        'benefits': 'A pain diary helps identify patterns and provides valuable information for healthcare providers. Tracking activities and triggers allows for a more personalized approach to pain management and treatment.'
    },
    20: {
        'activity': 'Hydration',
        'tip': 'Drink an adequate amount of water throughout the day. Carry a water bottle to remind yourself to stay hydrated.',
        'benefits': 'Proper hydration prevents dehydration, which can contribute to muscle tension and headaches. It supports overall health and aids in the optimal functioning of various bodily processes.'
    },
    21: {
        'activity': 'Gentle Yoga',
        'instructions': 'Practice gentle yoga poses, such as Child\'s Pose, Downward Dog, and Cat-Cow stretches. Follow a beginner-friendly yoga routine.',
        'benefits': 'Gentle yoga promotes relaxation, improves circulation, and reduces muscle tension. The poses enhance flexibility and body awareness, contributing to an overall sense of well-being.'
    },
    22: {
        'activity': 'Stress Management',
        'tip': 'Incorporate stress-reducing techniques into your daily routine. Find activities that bring joy and relaxation, such as hobbies or spending time in nature.',
        'benefits': 'Managing stress is crucial for reducing chronic pain. Activities like mindfulness, meditation, or engaging in enjoyable hobbies contribute to an improved mood and overall well-being.'
    },
    23: {
        'activity': 'Shoulder Rolls',
        'instructions': 'Sit or stand comfortably. Roll your shoulders backward in a circular motion for 15-30 seconds. Repeat in the opposite direction.',
        'benefits': 'Shoulder rolls relax shoulder muscles, reducing tension that may contribute to headaches. This simple exercise is effective in alleviating stiffness and promoting better posture.'
    },
    24: {
        'activity': 'Acupressure',
        'instructions': 'Use your index finger and thumb to apply firm pressure to the webbing between your thumb and index finger of the opposite hand. Hold for 10 seconds and release. Repeat on the other hand.',
        'benefits': 'Acupressure stimulates the flow of energy and blood in the body, relieving headache pain and tension. It targets specific pressure points to promote overall well-being.'
    },
    25: {
        'activity': 'Warm or Cold Compress',
        'instructions': 'Apply a warm or cold compress to the forehead or neck. Use a cloth to protect your skin. Apply for 15 minutes, then take a break before reapplying if needed.',
        'benefits': 'Warm or cold compresses provide comfort and help reduce headache symptoms. Cold packs constrict blood vessels, while heat packs relax muscles and improve blood circulation.'
    },
    26: {
        'activity': 'Mindfulness and Relaxation Techniques',
        'tip': 'Incorporate mindfulness practices into your daily routine. Find moments for relaxation, whether through deep breathing, visualization, or short meditation sessions.',
        'benefits': 'Mindfulness and relaxation techniques calm the nervous system and help manage pain triggers. They promote a sense of tranquility and enhance overall well-being.'
    },
    27: {
        'activity': 'Create a Comfortable Environment',
        'tip': 'Ensure your living and working spaces are ergonomically friendly. Adjust your chair, desk, and computer monitor to promote better posture.',
        'benefits': 'Creating a comfortable environment reduces strain on muscles and joints. Ergonomic adjustments contribute to a healthier and more pain-free physical experience.'
    },
    28: {
        'activity': 'Regular Exercise',
        'tip': 'Engage in regular physical activity, such as walking, swimming, or cycling. Choose activities that you enjoy and can incorporate into your routine.',
        'benefits': 'Regular exercise enhances overall well-being, reduces stress, and promotes better sleep. It contributes to pain management by improving circulation, flexibility, and strength.'
    }
}
lower_back_pain = {
    1: {
        'activity': 'Pelvic Clock Exercise',
        'instructions': 'Lie on your back with knees bent. Imagine your pelvis as the center of a clock and tilt it in various directions (12, 3, 6, 9 o\'clock positions). Begin with slow, controlled movements, gradually increasing the range of motion. Repeat for 10 minutes.',
        'benefits': 'Promotes mobility and flexibility in the pelvis and lower back, enhancing overall stability and reducing stiffness.'
    },
    2: {
        'activity': 'Knee-to-Chest Stretch',
        'instructions': 'Lie on your back, bring one knee toward your chest, and hold for 15-30 seconds. Switch legs and repeat. Perform gentle rocking motions while holding the stretch. Repeat 5 times on each side.',
        'benefits': 'Relieves tension in the lower back, improves hip flexibility, and stretches the muscles surrounding the spine.'
    },
    3: {
        'activity': 'Maintain a Regular Sleep Schedule',
        'tip': 'Ensure you get 7-9 hours of quality sleep each night. Establish a consistent sleep routine, including a relaxing pre-bedtime ritual.',
        'benefits': 'Adequate sleep supports overall well-being, enhances recovery, and contributes to effective pain management.'
    },
    4: {
        'activity': 'Wall Sits',
        'instructions': 'Stand with your back against a wall and lower into a seated position, keeping your back against the wall. Hold for 15-30 seconds. Gradually increase the duration to 1 minute over the week.',
        'benefits': 'Strengthens the muscles in the lower back, hips, and thighs, promoting stability and reducing the risk of lower back pain.'
    },
    5: {
        'activity': 'Modified Cobra Stretch',
        'instructions': 'Lie on your stomach, place your hands under your shoulders, and lift your upper body while keeping your pelvis on the floor. Hold for a few seconds and lower back down. Perform 10 repetitions.',
        'benefits': 'Stretches the spine, improves posture, and helps alleviate tension in the lower back.'
    },
    6: {
        'activity': 'Quadruped Opposite Arm and Leg Raise',
        'instructions': 'Start on hands and knees. Lift your right arm and left leg straight out, hold for a few seconds, and lower. Switch sides. Perform 3 sets of 10 repetitions on each side.',
        'benefits': 'Enhances core stability, strengthens the lower back and improves coordination.'
    },
    7: {
        'activity': 'Partial Crunches',
        'instructions': 'Lie on your back with knees bent. Tighten your abdominal muscles and lift your head and shoulders off the ground. Hold for a few seconds and lower back down. Complete 3 sets of 15 repetitions.',
        'benefits': 'Strengthens the abdominal muscles, supporting the lower back and improving core strength.'
    },
    8: {
        'activity': 'Hot and Cold Therapy',
        'tip': 'Use hot or cold packs as needed for 15-20 minutes. Apply cold packs for acute pain and inflammation, and warm packs for muscle relaxation.',
        'benefits': 'Provides comfort, reduces inflammation, and alleviates pain in specific areas.'
    },
    9: {
        'activity': 'Pain Diary',
        'tip': 'Record daily activities, pain levels, and potential triggers. Include details about sleep, diet, and exercise.',
        'benefits': 'Helps identify patterns, providing valuable information for healthcare providers and aiding in personalized pain management.'
    },
    10: {
        'activity': 'Seated Forward Bend',
        'instructions': 'Sit with legs extended, hinge at your hips, and reach toward your toes. Hold for 15-30 seconds. Perform gentle pulsing movements while holding the stretch. Repeat 5 times.',
        'benefits': 'Stretches the hamstrings, lower back, and promotes flexibility in the spine.'
    },
    11: {
        'activity': 'Pelvic Tilt',
        'instructions': 'Lie on your back with knees bent. Tighten your abdominal muscles, press your lower back into the floor, and hold for a few seconds. Release and repeat. Perform 3 sets of 12 repetitions.',
        'benefits': 'Strengthens the core muscles, improves pelvic stability, and reduces lower back strain.'
    },
    12: {
        'activity': 'Stress Management',
        'tip': 'Practice stress-reducing techniques such as mindfulness meditation or deep breathing exercises for 15-20 minutes.',
        'benefits': 'Reduces stress, lowers cortisol levels, and contributes to overall well-being and pain management.'
    },
    13: {
        'activity': 'Maintain a Regular Sleep Schedule',
        'tip': 'Ensure you get 7-9 hours of quality sleep each night. Establish a consistent sleep routine, including a relaxing pre-bedtime ritual.',
        'benefits': 'Adequate sleep supports overall well-being, enhances recovery, and contributes to effective pain management.'
    },
    14: {
        'activity': 'Lumbar Rotation Exercise',
        'instructions': 'Lie on your back, knees bent, and gently rotate your knees to one side while keeping your shoulders on the ground. Hold for 15-30 seconds and repeat on the other side. Perform 2 sets on each side.',
        'benefits': 'Enhances flexibility in the lower back, releases tension, and improves spinal mobility.'
    },
    15: {
        'activity': 'Prone Press-Up',
        'instructions': 'Lie facedown, place your hands under your shoulders, and press your upper body up, keeping your pelvis on the floor. Hold for a few seconds and lower back down. Complete 3 sets of 10 repetitions.',
        'benefits': 'Stretches the spine, strengthens the lower back muscles, and improves overall back flexibility.'
    },
    16: {
        'activity': 'Social Connection',
        'tip': 'Connect with friends or family members. Share your experiences and feelings.',
        'benefits': 'Social support positively impacts mental and emotional well-being, influencing how pain is perceived.'
    },
    17: {
        'activity': 'Mind-Body Practices',
        'tip': 'Explore mind-body practices like yoga or tai chi for 20-30 minutes.',
        'benefits': 'Combines gentle movement with mindfulness, promoting relaxation, flexibility, and mental well-being.'
    },
    18: {
        'activity': 'Bridge Exercise',
        'instructions': 'Lie on your back with knees bent. Lift your hips toward the ceiling, creating a straight line from shoulders to knees. Hold for a few seconds and lower back down. Perform 3 sets of 12 repetitions.',
        'benefits': 'Strengthens the lower back, glutes, and improves overall core stability.'
    },
    19: {
        'activity': 'Hydration',
        'tip': 'Drink an adequate amount of water throughout the day. Aim for at least 8 glasses.',
        'benefits': 'Prevents dehydration, which can contribute to muscle tension and headaches, supporting overall health.'
    },
    20: {
        'activity': 'Mindfulness and Relaxation Techniques',
        'tip': 'Incorporate mindfulness practices into your daily routine. Focus on your breath or use guided imagery for 15-20 minutes.',
        'benefits': 'Calms the nervous system, reduces stress, and helps manage pain triggers.'
    },
    21: {
        'activity': 'Healthy Diet',
        'tip': 'Maintain a balanced diet, avoiding foods that may trigger inflammation or exacerbate pain. Include fruits, vegetables, and lean proteins.',
        'benefits': 'Supports overall health, reduces inflammation, and helps manage potential pain triggers.'
    },
    22: {
        'activity': 'Leg Raises',
        'instructions': 'Lie on your back and lift one leg at a time toward the ceiling, keeping the other leg bent. Hold for a few seconds and lower. Alternate legs. Complete 3 sets of 15 repetitions.',
        'benefits': 'Strengthens the abdominal muscles and lower back, improving core strength and stability.'
    },
    23: {
        'activity': 'Cat-Cow Stretch',
        'instructions': 'Start on your hands and knees. Arch your back upward (cat position), then lower it down while lifting your head (cow position). Repeat in a flowing motion. Perform for 10 minutes.',
        'benefits': 'Improves flexibility and mobility in the spine, releases tension in the back and neck.'
    },
    24: {
        'activity': 'Pain Diary',
        'tip': 'Record daily activities, pain levels, and potential triggers. Include details about sleep, diet, and exercise.',
        'benefits': 'Helps identify patterns, providing valuable information for healthcare providers and aiding in personalized pain management.'
    },
    25: {
        'activity': 'Pelvic Tilt',
        'instructions': 'Lie on your back with knees bent. Tighten your abdominal muscles, press your lower back into the floor, and hold for a few seconds. Release and repeat. Perform 3 sets of 12 repetitions.',
        'benefits': 'Strengthens the core muscles, improves pelvic stability, and reduces lower back strain.'
    },
    26: {
        'activity': 'Knee-to-Chest Stretch',
        'instructions': 'Lie on your back, bring one knee toward your chest, and hold for 15-30 seconds. Switch legs and repeat. Perform gentle rocking motions while holding the stretch. Repeat 5 times on each side.',
        'benefits': 'Relieves tension in the lower back, improves hip flexibility, and stretches the muscles surrounding the spine.'
    },
    27: {
        'activity': 'Healthy Diet',
        'tip': 'Maintain a balanced diet, avoiding foods that may trigger inflammation or exacerbate pain. Include fruits, vegetables, and lean proteins.',
        'benefits': 'Supports overall health, reduces inflammation, and helps manage potential pain triggers.'
    },
    28: {
        'activity': 'Pelvic Clock Exercise',
        'instructions': 'Lie on your back with knees bent. Imagine your pelvis as the center of a clock and tilt it in various directions (12, 3, 6, 9 o\'clock positions). Begin with slow, controlled movements, gradually increasing the range of motion. Repeat for 10 minutes.',
        'benefits': 'Promotes mobility and flexibility in the pelvis and lower back, enhancing overall stability and reducing stiffness.'
    }
}
upper_back_pain = {
    1: {
        'activity': 'Scapular Wall Slide',
        'instructions': 'Stand with your back against a wall. Keep your arms against the wall and slide them upward, extending as far as comfortable. Hold for a few seconds, then slowly lower your arms. This exercise targets the muscles around your shoulder blades, enhancing their strength and improving the movement of your shoulder blades.',
        'benefits': 'Strengthens the muscles around the shoulder blades, promoting good posture and reducing upper back tension.'
    },
    2: {
        'activity': 'Healthy Diet',
        'tip': 'Focus on consuming a variety of nutrient-dense foods, including fruits, vegetables, lean proteins, and whole grains. A well-balanced diet provides essential nutrients for overall health and helps manage inflammation, a common factor in pain.',
        'benefits': 'Supports overall health, aids in weight management, and helps reduce inflammation, contributing to pain management.'
    },
    3: {
        'activity': 'Thoracic Rotation',
        'instructions': 'Sit or stand with your back straight. Rotate your upper body to one side, keeping your hips stable. Hold for 10-15 seconds, then return to the center and repeat on the other side. This movement enhances the mobility of your thoracic spine, reducing stiffness and promoting better posture.',
        'benefits': 'Improves thoracic spine mobility, reducing tension and discomfort in the upper back.'
    },
    4: {
        'activity': 'Neck Retraction Exercise',
        'instructions': 'Sit or stand with a straight spine. Gently tuck your chin towards your chest without tilting your head forward. Hold for 5-10 seconds, release, and repeat. This exercise strengthens the muscles in your neck and promotes proper alignment in the upper back.',
        'benefits': 'Strengthens neck muscles, reduces strain, and encourages better posture.'
    },
    5: {
        'activity': 'Maintain a Regular Sleep Schedule',
        'tip': 'Aim for 7-9 hours of sleep each night. Create a relaxing bedtime routine and maintain a consistent sleep schedule. Quality sleep is crucial for overall well-being and helps manage pain.',
        'benefits': 'Supports overall well-being, aids in healing, and contributes to pain management.'
    },
    6: {
        'activity': 'Chest Opener Stretch',
        'instructions': 'Sit or stand with your hands clasped behind your back. Straighten your arms and lift them slightly, opening your chest. Hold for 15-20 seconds. This stretch counteracts forward shoulder posture and alleviates tension in the chest and shoulders.',
        'benefits': 'Stretches the chest and front shoulder muscles, improving posture and reducing upper body tension.'
    },
    7: {
        'activity': 'Resistance Band Pull-Aparts',
        'instructions': 'Hold a resistance band in front of you with both hands. Pull the band apart, squeezing your shoulder blades together. Return to the starting position. This exercise targets the muscles between your shoulder blades, promoting upper back strength and good posture.',
        'benefits': 'Strengthens the muscles between the shoulder blades, improving posture and reducing upper back strain.'
    },
    8: {
        'activity': 'Pacing Activities',
        'tip': 'Break down tasks into smaller, manageable segments and take breaks as needed. Pacing activities helps avoid overexertion, minimizing the risk of pain flare-ups.',
        'benefits': 'Prevents overexertion, reduces the risk of pain flare-ups, and promotes consistent energy levels.'
    },
    9: {
        'activity': 'Levator Scapulae Stretch',
        'instructions': 'Sit or stand and gently tilt your head to one side, bringing your ear toward your shoulder. Use your hand to apply gentle pressure on the side of your head. Hold for 15-20 seconds and switch sides. This stretch targets the levator scapulae muscles, relieving tension in the upper back and neck.',
        'benefits': 'Stretches the levator scapulae muscles, reducing upper back tension and promoting flexibility.'
    },
    10: {
        'activity': 'Upper Back Extension',
        'instructions': 'Sit or stand with your hands clasped behind your lower back. Lift your arms slightly, opening your chest and arching your upper back. Hold for 10-15 seconds. This movement improves flexibility in the upper back and shoulders.',
        'benefits': 'Improves flexibility, reduces stiffness in the upper back, and promotes better posture.'
    },
    11: {
        'activity': 'Mind-Body Practices',
        'tip': 'Explore mind-body practices like yoga or tai chi. These activities combine gentle movement with mindfulness, promoting relaxation, and enhancing overall flexibility.',
        'benefits': 'Combines physical activity with mindfulness, reducing stress, and promoting overall well-being.'
    },
    12: {
        'activity': 'Upper Back Foam Rolling',
        'instructions': 'Use a foam roller to roll along the upper back muscles, focusing on areas of tension. Move slowly and gently. Roll for 2-3 minutes. Foam rolling releases tightness in the muscles and promotes blood flow, aiding in muscle recovery.',
        'benefits': 'Releases tension in the upper back muscles, improves blood circulation, and supports muscle recovery.'
    },
    13: {
        'activity': 'Social Connection',
        'tip': 'Maintain social connections and share experiences with supportive friends and family. Social support positively impacts mental and emotional well-being, influencing how pain is perceived.',
        'benefits': 'Boosts emotional well-being, reduces feelings of isolation, and positively affects pain perception.'
    },
    14: {
        'activity': 'Seated Thoracic Stretch',
        'instructions': 'Sit on the floor with your legs crossed. Place your right hand on the floor behind you and your left hand on your right knee. Twist to the right, feeling a stretch in your upper back. Hold for 15-20 seconds and switch sides. This stretch increases mobility in the thoracic spine.',
        'benefits': 'Increases thoracic spine mobility, reducing stiffness and promoting better posture.'
    },
    15: {
        'activity': 'Hydration',
        'tip': 'Drink an adequate amount of water throughout the day. Hydration is crucial for preventing dehydration, which can contribute to muscle tension and headaches.',
        'benefits': 'Maintains proper bodily functions, prevents dehydration-related issues, and supports overall health.'
    },
    16: {
        'activity': 'Shoulder Blade Squeeze',
        'instructions': 'Sit or stand with your shoulders relaxed. Squeeze your shoulder blades together, hold for 5-10 seconds, and then release. This exercise strengthens the muscles between your shoulder blades, improving upper back posture.',
        'benefits': 'Strengthens muscles between the shoulder blades, promoting good posture and reducing tension.'
    },
    17: {
        'activity': 'Mindfulness and Relaxation Techniques',
        'tip': 'Incorporate mindfulness practices into your daily routine. Techniques such as meditation and deep breathing calm the nervous system, helping manage pain triggers.',
        'benefits': 'Calms the nervous system, reduces stress, and helps manage pain triggers.'
    },
    18: {
        'activity': 'Upper Trapezius Stretch',
        'instructions': 'Sit or stand with your back straight. Tilt your head to one side, bringing your ear toward your shoulder. Hold for 15-20 seconds. This stretch specifically targets the upper trapezius muscles, relieving tension in the neck and shoulders.',
        'benefits': 'Relieves tension in the upper trapezius muscles, reducing discomfort in the neck and shoulders.'
    },
    19: {
        'activity': 'Regular Exercise',
        'tip': 'Engage in regular physical activity to improve overall health. Exercise enhances well-being, reduces stress, and promotes better sleep, contributing to pain management.',
        'benefits': 'Enhances overall well-being, reduces stress, and contributes to pain management through improved physical fitness.'
    },
    20: {
        'activity': 'Latissimus Dorsi Stretch',
        'instructions': 'Stand with one arm raised and bent at the elbow. Grab the raised elbow with your opposite hand and gently pull, feeling a stretch in the side of your back. Hold for 15-20 seconds and switch sides. This stretch improves flexibility in the latissimus dorsi muscles.',
        'benefits': 'Stretches the latissimus dorsi muscles, improving upper back flexibility.'
    },
    21: {
        'activity': 'Thoracic Extension',
        'instructions': 'Sit or stand with your hands clasped behind your head. Gently arch your upper back backward, opening your chest. Hold for 10-15 seconds. This movement promotes mobility in the thoracic spine and reduces stiffness.',
        'benefits': 'Improves thoracic spine mobility, reducing stiffness and promoting better posture.'
    },
    22: {
        'activity': 'Stress Management',
        'tip': 'Practice stress-reducing techniques such as mindfulness, meditation, or deep breathing exercises. Managing stress is crucial for reducing chronic pain.',
        'benefits': 'Reduces stress, a significant contributor to chronic pain, and promotes overall well-being.'
    },
    23: {
        'activity': 'Maintain a Regular Sleep Schedule',
        'tip': 'Ensure you get sufficient and consistent sleep each night. Adequate sleep supports overall well-being and helps manage pain.',
        'benefits': 'Supports overall well-being, aids in healing, and contributes to pain management.'
    },
    24: {
        'activity': 'Rotator Cuff Exercises',
        'instructions': 'Perform external and internal rotation exercises with a resistance band to strengthen the rotator cuff muscles. Hold for 10-15 seconds in each direction. This enhances stability in the shoulder joints, reducing upper back strain.',
        'benefits': 'Strengthens rotator cuff muscles, enhances shoulder joint stability, and reduces strain in the upper back.'
    },
    25: {
        'activity': 'Pectoral Stretch',
        'instructions': 'Stand in a doorway, place your hands on the door frame, and step forward. Hold for 15-20 seconds. This stretch opens up the chest and counteracts forward shoulder posture.',
        'benefits': 'Opens the chest and front shoulder muscles, reducing tension in the upper body.'
    },
    26: {
        'activity': 'Resistance Band Pull-Aparts',
        'instructions': 'Hold a resistance band in front of you with both hands. Pull the band apart, squeezing your shoulder blades together. Return to the starting position. This exercise strengthens the muscles between your shoulder blades and improves posture.',
        'benefits': 'Strengthens muscles between the shoulder blades, promoting good posture and reducing upper back strain.'
    },
    27: {
        'activity': 'Knee-to-Chest Stretch',
        'instructions': 'Lie on your back, bring one knee toward your chest, and hold for 15-20 seconds. Switch legs and repeat. This stretch relieves tension in the lower back and stretches the muscles.',
        'benefits': 'Relieves tension in the lower back, promoting flexibility and reducing discomfort.'
    },
    28: {
        'activity': 'Pain Diary',
        'tip': 'Keep a pain diary to track activities, symptoms, and potential triggers. Record the intensity and duration of pain. This helps identify patterns and provides valuable information for healthcare providers.',
        'benefits': 'Aids healthcare providers in understanding pain patterns, facilitating better treatment decisions, and enhancing overall pain management.'
    }
}
muscle_pain = {
    1: {
        'activity': 'Scapular Wall Slide',
        'instructions': 'Stand with your back against a wall. Keep your arms against the wall and slide them upward, extending as far as comfortable. Hold for a few seconds, then slowly lower your arms. This exercise targets the muscles around your shoulder blades, enhancing their strength and improving the movement of your shoulder blades, promoting good posture and reducing upper back tension.',
        'benefits': 'Strengthens the muscles around the shoulder blades, promoting good posture and reducing upper back tension.'
    },
    2: {
        'activity': 'Healthy Diet',
        'tip': 'Focus on consuming a variety of nutrient-dense foods, including fruits, vegetables, lean proteins, and whole grains. A well-balanced diet provides essential nutrients for overall health and helps manage inflammation, a common factor in pain.',
        'benefits': 'Supporting overall health, aiding in weight management, and helping reduce inflammation, contributing to pain management.'
    },
    3: {
        'activity': 'Thoracic Rotation',
        'instructions': 'Sit or stand with your back straight. Rotate your upper body to one side, keeping your hips stable. Hold for 10-15 seconds, then return to the center and repeat on the other side. This movement improves thoracic spine mobility, reducing stiffness and promoting better posture.',
        'benefits': 'Improves thoracic spine mobility, reducing tension and discomfort in the upper back.'
    },
    4: {
        'activity': 'Neck Retraction Exercise',
        'instructions': 'Sit or stand with a straight spine. Gently tuck your chin towards your chest without tilting your head forward. Hold for 5-10 seconds, release, and repeat. This exercise strengthens neck muscles and promotes proper alignment in the upper back.',
        'benefits': 'Strengthens neck muscles, reduces strain, and encourages better posture.'
    },
    5: {
        'activity': 'Maintain a Regular Sleep Schedule',
        'tip': 'Aim for 7-9 hours of sleep each night. Create a relaxing bedtime routine and maintain a consistent sleep schedule. Quality sleep is crucial for overall well-being and helps manage pain.',
        'benefits': 'Supports overall well-being, aids in healing, and contributes to pain management.'
    },
    6: {
        'activity': 'Chest Opener Stretch',
        'instructions': 'Sit or stand with your hands clasped behind your back. Straighten your arms and lift them slightly, opening your chest. Hold for 15-20 seconds. This stretch counteracts forward shoulder posture and alleviates tension in the chest and shoulders.',
        'benefits': 'Stretches the chest and front shoulder muscles, improving posture and reducing upper body tension.'
    },
    7: {
        'activity': 'Resistance Band Pull-Aparts',
        'instructions': 'Hold a resistance band in front of you with both hands. Pull the band apart, squeezing your shoulder blades together. Return to the starting position. This exercise targets the muscles between your shoulder blades, promoting upper back strength and good posture.',
        'benefits': 'Strengthens the muscles between the shoulder blades, promoting good posture and reducing upper back strain.'
    },
    8: {
        'activity': 'Pacing Activities',
        'tip': 'Break down tasks into smaller, manageable segments and take breaks as needed. Pacing activities helps avoid overexertion, minimizing the risk of pain flare-ups.',
        'benefits': 'Prevents overexertion, reduces the risk of pain flare-ups, and promotes consistent energy levels.'
    },
    9: {
        'activity': 'Levator Scapulae Stretch',
        'instructions': 'Sit or stand and gently tilt your head to one side, bringing your ear toward your shoulder. Use your hand to apply gentle pressure on the side of your head. Hold for 15-20 seconds and switch sides. This stretch targets the levator scapulae muscles, relieving tension in the upper back and neck.',
        'benefits': 'Stretches the levator scapulae muscles, reducing upper back tension and promoting flexibility.'
    },
    10: {
        'activity': 'Upper Back Extension',
        'instructions': 'Sit or stand with your hands clasped behind your lower back. Lift your arms slightly, opening your chest and arching your upper back. Hold for 10-15 seconds. This movement improves flexibility in the upper back and shoulders.',
        'benefits': 'Improves flexibility, reduces stiffness in the upper back, and promotes better posture.'
    },
    11: {
        'activity': 'Mind-Body Practices',
        'tip': 'Explore mind-body practices like yoga or tai chi. These activities combine gentle movement with mindfulness, promoting relaxation and enhancing overall flexibility.',
        'benefits': 'Combines physical activity with mindfulness, reducing stress, and promoting overall well-being.'
    },
    12: {
        'activity': 'Upper Back Foam Rolling',
        'instructions': 'Use a foam roller to roll along the upper back muscles, focusing on areas of tension. Move slowly and gently. Roll for 2-3 minutes. Foam rolling releases tension in the upper back muscles, improves blood circulation, and supports muscle recovery.',
        'benefits': 'Releases tension in the upper back muscles, improves blood circulation, and supports muscle recovery.'
    },
    13: {
        'activity': 'Social Connection',
        'tip': 'Maintain social connections and share experiences with supportive friends and family. Social support positively impacts mental and emotional well-being, influencing how pain is perceived.',
        'benefits': 'Boosts emotional well-being, reduces feelings of isolation, and positively affects pain perception.'
    },
    14: {
        'activity': 'Seated Thoracic Stretch',
        'instructions': 'Sit on the floor with your legs crossed. Place your right hand on the floor behind you and your left hand on your right knee. Twist to the right, feeling a stretch in your upper back. Hold for 15-20 seconds and switch sides. This stretch increases thoracic spine mobility.',
        'benefits': 'Increases thoracic spine mobility, reducing stiffness and promoting better posture.'
    },
    15: {
        'activity': 'Hydration',
        'tip': 'Drink an adequate amount of water throughout the day. Hydration is crucial for preventing dehydration, which can contribute to muscle tension and headaches.',
        'benefits': 'Maintains proper bodily functions, prevents dehydration-related issues, and supports overall health.'
    },
    16: {
        'activity': 'Shoulder Blade Squeeze',
        'instructions': 'Sit or stand with your shoulders relaxed. Squeeze your shoulder blades together, hold for 5-10 seconds, and then release. This exercise strengthens muscles between the shoulder blades, improving upper back posture.',
        'benefits': 'Strengthens muscles between the shoulder blades, promoting good posture and reducing tension.'
    },
    17: {
        'activity': 'Mindfulness and Relaxation Techniques',
        'tip': 'Incorporate mindfulness practices into your daily routine. Techniques such as meditation and deep breathing calm the nervous system, helping manage pain triggers.',
        'benefits': 'Calms the nervous system, reduces stress, and helps manage pain triggers.'
    },
    18: {
        'activity': 'Upper Trapezius Stretch',
        'instructions': 'Sit or stand with your back straight. Tilt your head to one side, bringing your ear toward your shoulder. Hold for 15-20 seconds. This stretch specifically targets the upper trapezius muscles, relieving tension in the neck and shoulders.',
        'benefits': 'Relieves tension in the upper trapezius muscles, reducing discomfort in the neck and shoulders.'
    },
    19: {
        'activity': 'Regular Exercise',
        'tip': 'Engage in regular physical activity to improve overall health. Exercise enhances well-being, reduces stress, and promotes better sleep, contributing to pain management.',
        'benefits': 'Enhances overall well-being, reduces stress, and contributes to pain management through improved physical fitness.'
    },
    20: {
        'activity': 'Latissimus Dorsi Stretch',
        'instructions': 'Stand with one arm raised and bent at the elbow. Grab the raised elbow with your opposite hand and gently pull, feeling a stretch in the side of your back. Hold for 15-20 seconds and switch sides. This stretch improves flexibility in the latissimus dorsi muscles.',
        'benefits': 'Stretches the latissimus dorsi muscles, improving upper back flexibility.'
    },
    21: {
        'activity': 'Thoracic Extension',
        'instructions': 'Sit or stand with your hands clasped behind your head. Gently arch your upper back backward, opening your chest. Hold for 10-15 seconds. This movement promotes thoracic spine mobility, reduces stiffness, and promotes better posture.',
        'benefits': 'Improves thoracic spine mobility, reduces stiffness, and promotes better posture.'
    },
    22: {
        'activity': 'Stress Management',
        'tip': 'Practice stress-reducing techniques such as mindfulness, meditation, or deep breathing exercises. Managing stress is crucial for reducing chronic pain.',
        'benefits': 'Reduces stress, a significant contributor to chronic pain, and promotes overall well-being.'
    },
    23: {
        'activity': 'Maintain a Regular Sleep Schedule',
        'tip': 'Ensure you get sufficient and consistent sleep each night.',
        'benefits': 'Supports overall well-being, aids in healing, and contributes to pain management.'
    },
    24: {
        'activity': 'Rotator Cuff Exercises',
        'instructions': 'Perform external and internal rotation exercises with a resistance band. Strengthen the rotator cuff muscles. Hold for 10-15 seconds in each direction.',
        'benefits': 'This exercise strengthens rotator cuff muscles, enhances shoulder joint stability, and reduces strain in the upper back.'
    },
    25: {
        'activity': 'Pectoral Stretch',
        'instructions': 'Stand in a doorway, place your hands on the door frame, and step forward. Hold for 15-20 seconds. This stretch opens the chest and front shoulder muscles, reducing tension in the upper body.',
        'benefits': 'Opens the chest and front shoulder muscles, reducing tension in the upper body.'
    },
    26: {
        'activity': 'Resistance Band Pull-Aparts',
        'instructions': 'Hold a resistance band in front of you with both hands. Pull the band apart, squeezing your shoulder blades together. Return to the starting position. This exercise strengthens muscles between the shoulder blades, promoting good posture and reducing upper back strain.',
        'benefits': 'Strengthens muscles between the shoulder blades, promoting good posture and reducing upper back strain.'
    },
    27: {
        'activity': 'Knee-to-Chest Stretch',
        'instructions': 'Lie on your back, bring one knee toward your chest, and hold for 15-20 seconds. Switch legs and repeat. This stretch relieves tension in the lower back, promoting flexibility and reducing discomfort.',
        'benefits': 'Relieves tension in the lower back, promotes flexibility, and reduces discomfort.'
    },
    28: {
        'activity': 'Pain Diary',
        'tip': 'Keep a pain diary to track activities, symptoms, and potential triggers. Record the intensity and duration of pain.',
        'benefits': 'Aids healthcare providers in understanding pain patterns, facilitates better treatment decisions, and enhances overall pain management.'
    }
}
neck_pain = {
    1: {
        'activity': 'Neck Rotation Stretch',
        'instructions': 'Slowly tilt your head to one side, bringing your ear towards your shoulder. Hold for 15-30 seconds and repeat on the other side. Perform gentle neck rotations as well.',
        'benefits': 'This stretch helps relieve tension in the neck muscles and improves flexibility, promoting a wider range of motion in the neck.'
    },
    2: {
        'activity': 'Shoulder Blade Squeeze',
        'instructions': 'Sit or stand with your shoulders relaxed. Squeeze your shoulder blades together, hold for a few seconds, and then release.',
        'benefits': 'Strengthening the muscles between the shoulder blades through this exercise promotes better posture and reduces tension in the neck and upper back.'
    },
    3: {
        'activity': 'Neck Isometrics',
        'instructions': 'Place your hand on the side of your head and press your head into your hand, resisting the movement. Hold for a few seconds and repeat on the other side.',
        'benefits': 'Neck isometrics help in building strength in the neck muscles without the need for extensive movement, contributing to better stability.'
    },
    4: {
        'activity': 'Scalene Stretch',
        'instructions': 'Sit or stand with a straight spine. Reach your right arm down and grab the side of your chair. Tilt your head to the left, feeling a stretch along the right side of your neck. Hold for 15-30 seconds and switch sides.',
        'benefits': 'Stretching the scalene muscles on the sides of the neck alleviates tension and improves flexibility in the neck and upper shoulders.'
    },
    5: {
        'activity': 'Healthy Diet',
        'tip': 'Maintain a balanced diet, avoiding foods that may trigger inflammation or exacerbate pain.',
        'benefits': 'A well-balanced diet supports overall health, aids in weight management, and helps reduce inflammation, contributing to pain management.'
    },
    6: {
        'activity': 'Forward and Backward Head Movements',
        'instructions': 'Gently nod your head forward and backward, moving through a pain-free range of motion.',
        'benefits': 'This simple movement exercise improves flexibility and reduces tension in the neck, promoting a broader range of motion.'
    },
    7: {
        'activity': 'Hydration',
        'tip': 'Drink an adequate amount of water throughout the day.',
        'benefits': 'Proper hydration is crucial for preventing dehydration, which can contribute to muscle tension, headaches, and overall discomfort.'
    },
    8: {
        'activity': 'Stress Management',
        'tip': 'Practice stress-reducing techniques such as mindfulness, meditation, or deep breathing exercises.',
        'benefits': 'Effectively managing stress is essential for reducing chronic pain, as it positively impacts overall well-being.'
    },
    9: {
        'activity': 'Neck Stretches',
        'instructions': 'Slowly tilt your head to one side, bringing your ear towards your shoulder. Hold for 15-30 seconds and repeat on the other side. Perform gentle neck rotations as well.',
        'benefits': 'This set of stretches relieves tension in the neck muscles and improves flexibility, aiding in overall neck health.'
    },
    10: {
        'activity': 'Upper Back Foam Rolling',
        'instructions': 'Use a foam roller to roll along the upper back and neck muscles, focusing on areas of tension. Move slowly and gently.',
        'benefits': 'Foam rolling releases tension in the upper back and neck muscles, promoting blood circulation and aiding in muscle recovery.'
    },
    11: {
        'activity': 'Pacing Activities',
        'tip': 'Break tasks into smaller, manageable segments and take breaks as needed.',
        'benefits': 'Pacing activities helps avoid overexertion, reducing the risk of pain flare-ups and maintaining consistent energy levels.'
    },
    12: {
        'activity': 'Neck Extension Exercise',
        'instructions': 'Sit or stand with your back straight. Slowly tilt your head backward, looking up towards the ceiling. Hold for a few seconds and return to the starting position.',
        'benefits': 'This exercise strengthens the muscles at the front of the neck, improving neck stability and range of motion.'
    },
    13: {
        'activity': 'Chin Tucks',
        'instructions': 'Sit or stand with a straight spine. Gently tuck your chin towards your chest without tilting your head forward. Hold for a few seconds and release.',
        'benefits': 'Chin tucks strengthen neck muscles and promote proper alignment, reducing strain on the neck and upper back.'
    },
    14: {
        'activity': 'Upper Trapezius Stretch',
        'instructions': 'Sit or stand with your back straight. Tilt your head to one side, bringing your ear toward your shoulder. Hold for 15-30 seconds and repeat on the other side.',
        'benefits': 'Relieving tension in the upper trapezius muscles through this stretch contributes to overall neck and shoulder comfort.'
    },
    15: {
        'activity': 'Maintain a Regular Sleep Schedule',
        'tip': 'Ensure you get sufficient and consistent sleep each night.',
        'benefits': 'Adequate sleep supports overall well-being, aids in healing, and contributes significantly to pain management.'
    },
    16: {
        'activity': 'Side-to-Side Head Tilt',
        'instructions': 'Tilt your head to one side, bringing your ear towards your shoulder. Hold for a few seconds and tilt to the other side.',
        'benefits': 'This movement promotes flexibility and reduces stiffness in the neck, enhancing overall neck comfort.'
    },
    17: {
        'activity': 'Ear-to-Shoulder Stretch',
        'instructions': 'Tilt your head to one side, bringing your ear towards your shoulder. Hold for 15-30 seconds and repeat on the other side.',
        'benefits': 'Stretching the muscles along the side of the neck contributes to improved flexibility and reduced tension.'
    },
    18: {
        'activity': 'Rotational Head Movements',
        'instructions': 'Turn your head to one side, looking over your shoulder. Hold for a few seconds and turn to the other side.',
        'benefits': 'Enhancing mobility in the neck through rotational movements reduces stiffness and supports overall neck health.'
    },
    19: {
        'activity': 'Rotator Cuff Exercises',
        'instructions': 'Perform external and internal rotation exercises with a resistance band. Strengthen the rotator cuff muscles. Hold for 10-15 seconds in each direction.',
        'benefits': 'Strengthening rotator cuff muscles enhances shoulder joint stability, reducing strain in the upper back and neck.'
    },
    20: {
        'activity': 'Neck Flexor Stretch',
        'instructions': 'Sit or stand with a straight spine. Gently lower your chin towards your chest, feeling a stretch in the back of your neck. Hold for 15-30 seconds.',
        'benefits': 'This stretch targets the muscles at the back of the neck, promoting flexibility and reducing tension.'
    },
    21: {
        'activity': 'Shoulder Rolls',
        'instructions': 'Roll your shoulders backward in a circular motion for 15-30 seconds. Repeat in the opposite direction.',
        'benefits': 'Shoulder rolls help relax shoulder muscles, reducing tension in the neck and upper back.'
    },
    22: {
        'activity': 'Neck Rotation Stretch',
        'instructions': 'Turn your head to one side, bringing your chin towards your shoulder. Hold for 15-30 seconds and repeat on the other side.',
        'benefits': 'Repeating the neck rotation stretch increases flexibility and reduces stiffness in the neck.'
    },
    23: {
        'activity': 'Upper Trapezius Stretch',
        'instructions': 'Sit or stand with your back straight. Tilt your head to one side, bringing your ear toward your shoulder. Hold for 15-30 seconds and repeat on the other side.',
        'benefits': 'Relieving tension in the upper trapezius muscles enhances overall neck and shoulder comfort.'
    },
    24: {
        'activity': 'Upper Back Foam Rolling',
        'instructions': 'Use a foam roller to roll along the upper back and neck muscles, focusing on areas of tension. Move slowly and gently.',
        'benefits': 'Foam rolling releases tension in the upper back and neck muscles, promoting blood circulation and aiding in muscle recovery.'
    },
    25: {
        'activity': 'Knee-to-Chest Stretch',
        'instructions': 'Lie on your back, bring one knee toward your chest, and hold for 15-20 seconds. Switch legs and repeat.',
        'benefits': 'This stretch relieves tension in the lower back, promoting flexibility and reducing discomfort.'
    },
    26: {
        'activity': 'Resistance Band Pull-Aparts',
        'instructions': 'Hold a resistance band in front of you with both hands. Pull the band apart, squeezing your shoulder blades together. Return to the starting position.',
        'benefits': 'Strengthening muscles between the shoulder blades through pull-aparts improves posture and reduces upper back strain.'
    },
    27: {
        'activity': 'Neck Extension Exercise',
        'instructions': 'Sit or stand with your back straight. Slowly tilt your head backward, looking up towards the ceiling. Hold for a few seconds and return to the starting position.',
        'benefits': 'This exercise strengthens the muscles at the front of the neck, improving neck stability and range of motion.'
    },
    28: {
        'activity': 'Pain Diary',
        'tip': 'Keep a pain diary to track activities, symptoms, and potential triggers. Record the intensity and duration of pain.',
        'benefits': 'A pain diary aids healthcare providers in understanding pain patterns, facilitating better treatment decisions, and enhancing overall pain management.'
    }
}

# Fetch data from Sheety endpoints
email_responses = requests.get(email_responses_url, headers=headers).json()['formResponses1']
form_responses = requests.get(form_responses_url, headers=headers).json()['formResponses1']

# Create dictionaries to store data with timestamps as keys
email_data = {entry['timestamp']: entry for entry in email_responses}
form_data = {entry['timestamp']: entry for entry in form_responses}

# Load existing users' data from JSON file or create a new dictionary if the file doesn't exist
json_filename = 'users_data.json'
try:
    with open(json_filename, 'r') as json_file:
        users_dict = json.load(json_file)
except FileNotFoundError:
    users_dict = {}

# Find matching timestamps
matching_timestamps = set(email_data.keys()) & set(form_data.keys())

if matching_timestamps:
    print("Matching timestamps found:")
    for timestamp in matching_timestamps:
        email_entry = email_data[timestamp]
        form_entry = form_data[timestamp]
        user_email = email_entry['yourEmailAddress']
        user_name = form_entry['whatIsYourName']
        pain_type = form_entry['whatTypeOfPainAreYouFeeling']

        # Check if user already exists
        if user_email not in users_dict:
            # Store user information in the dictionary
            users_dict[user_email] = {
                'name': user_name,
                'pain_type': pain_type,
                'day': 0
            }

            print(f"Email: {user_email}, Name: {user_name}, Pain Type: {pain_type} - Added to Users Dictionary")
        else:
            print(f"Email: {user_email} already exists in Users Dictionary. Skipping.")

            # Update the 'day' attribute for existing users
            users_dict[user_email]['day'] = users_dict[user_email]['day'] + 1  # Replace 'your_updated_value' with the new day value
            print(f"Updated day for user {user_email}: {users_dict[user_email]['day']}")

else:
    print("No matching timestamps found.")

def send_email(sender_email, receiver_email, subject, body):
    # Email configuration
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Attach the body of the email
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server and send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('serenelabs.team@gmail.com', 'hqbu aoju yckk ryti')

        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
    finally:
        server.quit()

users_to_remove = []
for user_email, user_data in users_dict.items():
    if user_data['day'] == 29:
        # Send thank you message
        subject = f"Thank You - End of 28-day Pain Challenge!"
        message = f"Hello {user_data['name']},\nThank you for completing the 28-day pain challenge! We appreciate your participation and hope this little challenge has helped you out.\nBest regards, \nSerenelabs Team"
        send_email(sender_email="serenelabs.team@gmail.com", receiver_email=user_email, subject=subject, body=message)

        # Mark user for removal
        users_to_remove.append(user_email)

# Remove marked users from the dictionary
for user_email in users_to_remove:
    del users_dict[user_email]
    print(f"User {user_email} removed from the dictionary.")

# Save the updated dictionary back to the JSON file
with open(json_filename, 'w') as json_file:
    json.dump(users_dict, json_file)


# Save the updated dictionary back to the JSON file
with open(json_filename, 'w') as json_file:
    json.dump(users_dict, json_file)

for user in users_dict:
    if users_dict[user]['pain_type'] == 'Neck pain':
        day = users_dict[user]['day']
        try:
            instructions = neck_pain[day]['instructions']
        except KeyError:
            instructions = neck_pain[day]['tip']
        subject = f"Welcome to Day {users_dict[user]['day']} of 28-day pain challenge!"
        message = f"Hello {users_dict[user]['name']},\nToday you are going to do: {instructions}.\n{neck_pain[day]['benefits']}"
        send_email(sender_email="serenelabs.team@gmail.com", receiver_email=user, subject=subject, body=message)
    elif users_dict[user]['pain_type'] == 'Lower back pain':
        day = users_dict[user]['day']
        try:
            instructions = neck_pain[day]['instructions']
        except KeyError:
            instructions = neck_pain[day]['tip']
        subject = f"Welcome to Day {users_dict[user]['day']} of 28-day pain challenge!"
        message = f"Hello {users_dict[user]['name']},\nToday you are going to do: {lower_back_pain[day]['activity']}.\n{instructions}\n{lower_back_pain[day]['benefits']}"
        send_email(sender_email="serenelabs.team@gmail.com", receiver_email=user, subject=subject, body=message)
    elif users_dict[user]['pain_type'] == 'Upper back pain':
        day = users_dict[user]['day']
        try:
            instructions = neck_pain[day]['instructions']
        except KeyError:
            instructions = neck_pain[day]['tip']
        subject = f"Welcome to Day {users_dict[user]['day']} of 28-day pain challenge!"
        message = f"Hello {users_dict[user]['name']},\nToday you are going to do: {upper_back_pain[day]['activity']}.\n{instructions}\n{upper_back_pain[day]['benefits']}"
        send_email(sender_email="serenelabs.team@gmail.com", receiver_email=user, subject=subject, body=message)
    elif users_dict[user]['pain_type'] == 'Muscle pain':
        day = users_dict[user]['day']
        try:
            instructions = neck_pain[day]['instructions']
        except KeyError:
            instructions = neck_pain[day]['tip']
        subject = f"Welcome to Day {users_dict[user]['day']} of 28-day pain challenge!"
        message = f"Hello {users_dict[user]['name']},\nToday you are going to do: {muscle_pain[day]['activity']}.\n{instructions}\n{muscle_pain[day]['benefits']}"
        send_email(sender_email="serenelabs.team@gmail.com", receiver_email=user, subject=subject, body=message)
    elif users_dict[user]['pain_type'] == 'Headaches':
        day = users_dict[user]['day']
        try:
            instructions = neck_pain[day]['instructions']
        except KeyError:
            instructions = neck_pain[day]['tip']
        subject = f"Welcome to Day {users_dict[user]['day']} of 28-day pain challenge!"
        message = f"Hello {users_dict[user]['name']},\nToday you are going to do: {headaches[day]['activity']}.\n{instructions}\n{headaches[day]['benefits']}"
        send_email(sender_email="serenelabs.team@gmail.com", receiver_email=user, subject=subject, body=message)
        
send_email(sender_email="serenelabs.team@gmail.com", receiver_email="serenelabs.team@gmail.com", subject="Daily Emails", body="Emails sent successfully!")