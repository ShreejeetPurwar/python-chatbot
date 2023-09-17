$(document).ready(function() {
    $("#chat-form").on("submit", function(e) {
        e.preventDefault();
        let user_input = $("#user_input").val().trim();
        let conversation_history = $("#conversation_history").val();

        if (user_input.toLowerCase() === "quit") {
            location.reload();
            return;
        }

        $("#chat-history").append(`<p><b>You:</b> ${user_input}</p>`);
        $("#user_input").val("");

        $.ajax({
            url: "/chat",
            method: "POST",
            data: {
                user_input: user_input,
                conversation_history: conversation_history
            },
            success: function(data) {
                $("#chat-history").append(`<p><b>Chatbot:</b> ${data.response}</p>`);
                $("#conversation_history").val(data.conversation_history);
                $("#chat-history").scrollTop($("#chat-history")[0].scrollHeight);
            }
        });
    });
});
