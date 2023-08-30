document.addEventListener("DOMContentLoaded", function () {
    const submitBtn = document.getElementById("submitBtn");
    const sendnewsboxTextarea = document.getElementById("sendnewsbox");

    submitBtn.addEventListener("click", function () {
        const sendnewsboxText = sendnewsTextarea.value;

        // Aqui, você pode adicionar código para enviar o feedback para o servidor,
        // salvar em um banco de dados ou fazer qualquer outra ação necessária.

        alert("Obrigado! Sua notícia logo será publicada");
        feedbackTextarea.value = ""; // Limpar o campo de feedback
    });
});
