<template>
    <slot name="top"></slot>
    <h1>자식 컴포넌트 머리</h1>
    <button>파일</button>
    <button>편집</button>
    <button>보기</button>
    <h1>자식 컴포넌트 꼬리</h1>
    <slot name="bottom"></slot>
</template>