function switch_language() {
    if ($('body.site-es').length>0)
    {
        $(".language-es").removeClass("currentLanguage");
        $(".language-en").addClass("currentLanguage");
        $(".language-es").insertAfter(".language-en");

    }
    if ($('body.site-en').length>0)
    {
        $(".language-en").removeClass("currentLanguage");
        $(".language-es").addClass("currentLanguage");
        $(".language-en").insertAfter(".language-es");
     }
}
$(document).ready(function() {
    switch_language();
});