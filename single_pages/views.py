from django.shortcuts import render


def landing(request): #22. landing(대문페이지)함수입력
    return render(
        request,
        'single_pages/landing.html', #23. templates파일 지정하고 single_pages/single_pages라는 폴더를 만들고 landing.html 파일을 만들고 이동한다.
    )


def about_me(request): #27. about_me에 대한 함수입력
    return render(
        request,
        'single_pages/about_me.html', #28. templates파일 지정하고 single_pages/single_pages/about_me.html을 만들고 그곳으로 이동한다.
    )
