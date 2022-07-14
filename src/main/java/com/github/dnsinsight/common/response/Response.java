package com.github.dnsinsight.common.response;

import lombok.AllArgsConstructor;
import lombok.Data;

import java.io.Serializable;

/**
 * @Author: Tachikoma
 * @Date: 2022-07-02 23:31
 * @Description:
 */
@Data
@AllArgsConstructor
public class Response<T extends Serializable> implements Serializable {
    private static final long serialVersionUID = 1L;

    private Integer code;
    private String message;
    private T data;

    public static Response success() {
        return new Response<>(ResponseCode.SUCCESS.code(), ResponseCode.SUCCESS.message(), null);
    }

    public static <T extends Serializable> Response success(T object) {
        return new Response<>(ResponseCode.SUCCESS.code(), ResponseCode.SUCCESS.message(), object);
    }

    public static Response fail(ResponseCode code) {
        return new Response<>(code.code(), code.message(),null);
    }
}
