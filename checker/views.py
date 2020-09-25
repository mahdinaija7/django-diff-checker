from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from checker.diffchecker import make_lines_equals, check_diff


# Create your views here.


def checker(request):
    if request.method == "POST":
        first_text = request.POST.get("first")
        second_text = request.POST.get("second")
        print(first_text.split("\n"))
        print(second_text.split("\n"))
    context = {}
    return render(request, "checker/index.html", context=context)


@require_http_methods(["POST"])
def apiJson(request):
    leftText = request.POST.get("first")
    rightText = request.POST.get("second")
    rightLines = list(map(lambda x: x.strip("\n"), rightText.split("\n")))
    leftLines = list(map(lambda x: x.strip("\n"), leftText.split("\n")))

    make_lines_equals(rightLines, leftLines)

    rightLines, leftLines = check_diff(leftLines, rightLines)
    return JsonResponse({"right": rightLines, "left": leftLines})

