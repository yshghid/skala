// login.js
import { isNotEmpty } from './validator.js';

document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("loginForm");

  form.addEventListener("submit", function (e) {
    e.preventDefault(); // 폼의 기본 제출 막기

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const isEmailValid = isNotEmpty(email, "이메일");
    const isPasswordValid = isNotEmpty(password, "비밀번호");

    if (isEmailValid && isPasswordValid) {
      window.location.href = "https://www.google.com";
    }
  });
});
