package com.github.dnsinsight.common.response;

public enum ResponseCode {
    SUCCESS(200,"SUCCES"),
    FAILURE(400,"FAILURE");

    private final Integer code;
    private final String message;

    ResponseCode(Integer code, String message) {
        this.code = code;
        this.message = message;
    }

    public Integer code() {
        return code;
    }

    public String message() {
        return message;
    }
}
