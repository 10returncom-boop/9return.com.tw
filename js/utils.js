/* =========================================================
   欣矩陣 ∞ 欣媒體 — utils.js
   主題切換（日夜＋跟隨系統）/ 側邊欄 / 捲動顯現 / FAQ / 篩選 / 回到頂部
   ========================================================= */
(function () {
  "use strict";

  /* ---------- 主題：日夜 ＋ 跟隨系統（localStorage 記憶） ---------- */
  var THEME_KEY = (window.SITE && window.SITE.themeKey) || "xinmatrix-theme";
  function applyTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme);
    try { localStorage.setItem(THEME_KEY, theme); } catch (e) {}
    var tog = document.getElementById("themeToggle");
    if (tog) {
      tog.setAttribute("aria-label", theme === "light" ? "切換至深色模式" : "切換至淺色模式");
      tog.title = theme === "light" ? "切換至深色模式" : "切換至淺色模式";
    }
  }
  function systemTheme() {
    return (window.matchMedia && window.matchMedia("(prefers-color-scheme: light)").matches) ? "light" : "dark";
  }
  function initTheme() {
    var saved = null;
    try { saved = localStorage.getItem(THEME_KEY); } catch (e) {}
    applyTheme(saved === "light" || saved === "dark" ? saved : systemTheme());
  }
  window.Theme = {
    toggle: function () {
      var cur = document.documentElement.getAttribute("data-theme");
      applyTheme(cur === "light" ? "dark" : "light");
    },
    reset: initTheme,
  };
  if (window.matchMedia) {
    window.matchMedia("(prefers-color-scheme: light)").addEventListener("change", function () {
      var saved = null;
      try { saved = localStorage.getItem(THEME_KEY); } catch (e) {}
      if (saved !== "light" && saved !== "dark") applyTheme(systemTheme());
    });
  }

  /* ---------- 側邊欄 Drawer ---------- */
  window.Drawer = {
    open: function () { var d = document.getElementById("drawer"); if (d) d.classList.add("open"); },
    close: function () { var d = document.getElementById("drawer"); if (d) d.classList.remove("open"); },
  };

  /* ---------- 捲動顯現 ---------- */
  function initReveal() {
    var els = document.querySelectorAll(".reveal");
    if (!("IntersectionObserver" in window)) { els.forEach(function (e) { e.classList.add("in"); }); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
    }, { threshold: 0.12 });
    els.forEach(function (e) { io.observe(e); });
  }

  /* ---------- FAQ ---------- */
  function initFaq() {
    document.querySelectorAll(".faq-item").forEach(function (item) {
      var q = item.querySelector(".faq-q");
      if (!q) return;
      q.addEventListener("click", function () {
        var isOpen = item.classList.contains("open");
        item.classList.toggle("open");
        var a = item.querySelector(".faq-a");
        if (a) { a.style.maxHeight = isOpen ? "0px" : a.scrollHeight + "px"; }
        q.setAttribute("aria-expanded", String(!isOpen));
      });
      var a = item.querySelector(".faq-a");
      if (a) { a.style.maxHeight = "0px"; q.setAttribute("aria-expanded", "false"); }
    });
  }

  /* ---------- 案例篩選 ---------- */
  function initFilter() {
    var bar = document.getElementById("caseFilter");
    if (!bar) return;
    var btns = bar.querySelectorAll(".filter-btn");
    var cards = document.querySelectorAll("[data-cat]");
    var empty = document.getElementById("caseEmpty");
    btns.forEach(function (b) {
      b.addEventListener("click", function () {
        btns.forEach(function (x) { x.classList.remove("active"); });
        b.classList.add("active");
        var f = b.getAttribute("data-filter");
        var shown = 0;
        cards.forEach(function (c) {
          var match = f === "全部" || c.getAttribute("data-cat").indexOf(f) !== -1;
          c.style.display = match ? "" : "none";
          if (match) shown++;
        });
        if (empty) empty.style.display = shown ? "none" : "block";
      });
    });
  }

  /* ---------- 回到頂部 ---------- */
  function initTop() {
    var btn = document.getElementById("toTop");
    if (!btn) return;
    function onScroll() { btn.classList.toggle("show", (window.scrollY || document.documentElement.scrollTop) > 500); }
    window.addEventListener("scroll", onScroll, { passive: true });
    btn.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: "smooth" }); });
    onScroll();
  }

  /* ---------- Header Popover / Dropdown 選單 ---------- */
  function initPopoverMenu() {
    var wrap = document.getElementById("popoverMenu");
    var btn = document.getElementById("menuToggle");
    if (!wrap || !btn) return;
    function setOpen(open) {
      wrap.classList.toggle("open", open);
      btn.setAttribute("aria-expanded", String(open));
    }
    btn.addEventListener("click", function (e) {
      e.stopPropagation();
      setOpen(!wrap.classList.contains("open"));
    });
    document.addEventListener("click", function (e) {
      if (!wrap.contains(e.target)) setOpen(false);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") setOpen(false);
    });
    wrap.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () { setOpen(false); });
    });
  }

  /* ---------- 主程式入口 ---------- */
  window.SiteInit = function () {
    initTheme();
    initReveal();
    initFaq();
    initFilter();
    initTop();
    initPopoverMenu();
    var b = document.getElementById("brandYear");
    if (b) b.textContent = new Date().getFullYear();
  };
})();
