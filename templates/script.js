// Get chart canvas element
var ctx = document.getElementById('emotionChart').getContext('2d');

// Initialize the bar chart
var emotionChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Video', 'Audio'],
        datasets: [{
            label: 'Confidence (%)',
            data: [0, 0], // Initial values
            backgroundColor: ['blue', 'red'],
            borderColor: ['blue', 'red'],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true,
                max: 100
            }
        }
    }
});

// Function to update UI with new values
function updateEmotionData(videoEmotion, videoConfidence, audioEmotion, audioConfidence) {
    document.getElementById("videoEmotion").innerText = videoEmotion;
    document.getElementById("videoConfidence").innerText = videoConfidence + "%";
    document.getElementById("audioEmotion").innerText = audioEmotion;
    document.getElementById("audioConfidence").innerText = audioConfidence + "%";

    // Calculate final emotion (basic logic)
    let finalEmotion = videoConfidence > audioConfidence ? videoEmotion : audioEmotion;
    document.getElementById("finalEmotion").innerText = finalEmotion;

    // Update chart data
    emotionChart.data.datasets[0].data = [videoConfidence, audioConfidence];
    emotionChart.update();
}

// Simulated function for real-time updates (Replace with backend API call)
function startLiveDetection() {
    alert("Live Emotion Detection Started...");

    // Simulating real-time updates every 2 seconds
    setInterval(() => {
        let emotions = ["happy", "neutral", "sad", "angry", "surprised"];
        let randomVideoEmotion = emotions[Math.floor(Math.random() * emotions.length)];
        let randomAudioEmotion = emotions[Math.floor(Math.random() * emotions.length)];
        let randomVideoConfidence = Math.floor(Math.random() * 100);
        let randomAudioConfidence = Math.floor(Math.random() * 100);

        updateEmotionData(randomVideoEmotion, randomVideoConfidence, randomAudioEmotion, randomAudioConfidence);
    }, 2000);
}
